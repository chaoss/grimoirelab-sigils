# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2017 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors:
#     Alberto Pérez García-Plaza <alpgarcia@bitergia.com>
#
"""Stuff to deal with index patterns from JSON files genrated by Kidash.
"""

import json
import logging

from unittest import TestCase


class Schema(object):
    """Intends to represent index structure in order
    to compare ES mappings against other compatible
    structures whose types does not match one to one,
    like Kibana types.

    schema_name     -- schema identifier
    __properties    -- dictionary of properties. Example:
        {
            'properties':{
                'author_name': {
                    'type': 'text',
                    'analyzed':  true,
                    'agg': true
                }
                ...
            }
        }

    """

    # List of types allowed for properties in this Schema
    __supported_types = ['text', 'keyword', 'number', 'date', 'boolean',
                         '_source', 'geo_point', 'object']
    __excluded_props = ['_id', '_index', '_score', '_source', '_type']
    # In mbox enriched indexes is_mbox is defined
    __excluded_props += ['is_gmane_message', 'is_mbox_message']
    # Cache from askbot could not include this field
    __excluded_props += ['is_askbot_comment']
    # Cache from confluence could not include this field
    __excluded_props += ['is_attachment', 'is_comment', 'is_new_page']

    def __init__(self, schema_name):
        self.schema_name = schema_name
        self.__properties = {}

    @staticmethod
    def check_type(src_type):
        """Checks if type is valid

        TypeError -- when type is not supported
        """
        if src_type not in Schema.__supported_types:
            raise TypeError("Type not supported:", src_type)

        return src_type

    def add_property(self, pname, ptype, analyzed=False, agg=False):
        """Adds a new property to the current schema. If there
        is already a property with same name, that property
        will be updated.

        Keyword arguments:
        pname       -- property names
        ptype       -- property type
        analyzed    -- is this property analyzed?
        agg         -- is this property aggregatable in Kibana?
        """
        # Exclude ES internal properties
        if pname not in self.__excluded_props:
            schema_type = self.check_type(ptype)
            self.__properties[pname] = {'type': schema_type}

            # Assuming that text is already giving us this information
            # implicitely
            # if analyzed:
            #     self.__properties[pname]['analyzed'] = True

            if agg:
                self.__properties[pname]['agg'] = True

    def get_properties(self):
        """Returns a dictionary containing all schema properties.

            Example:
            {
                'properties':{
                    'author_name': {
                        'type': 'text',
                        'analyzed':  true,
                        'agg': true
                    }
                    ...
                }
            }
        """
        return self.__properties

    def compare_properties(self, schema):
        """Compares two schemas. The schema used to call the method
        will be the one we compare from, in advance 'source schema'.
        The schema passed as parameter will be the 'target schema'.

        Returns -- dictionary {status, correct, missing, distinct, message}
            being:
                status 'OK' if all properties in source schema exist in target
                    schema with same values. 'KO' in other case.
                correct: list of properties that matches.
                missing: list of properties missing from target schema.
                distinct: list of properties in both schemas but having
                    with different values.
                message: a string with additional information.
        """
        test_case = TestCase('__init__')
        test_case.maxDiff = None

        status = 'OK'
        correct = []
        missing = []
        distinct = []
        msg = ''
        for pname, pvalue in self.get_properties().items():
            if pname not in schema.get_properties():
                missing.append(pname)
                msg = msg + '\n' + '* Missing property: ' + pname
                status = 'KO'
            else:
                try:
                    test_case.assertDictEqual(pvalue,
                                              schema.get_properties()[pname])
                    correct.append(pname)

                except AssertionError as e:
                    distinct.append(pname)
                    msg = "%s\n* Type mismatch: \n\t%s: %s" %\
                        (msg, pname, str(e).replace('\n', '\n\t'))
                    status = 'KO'

        return {'status': status, 'correct': correct, 'missing': missing,
                'distinct': distinct, 'msg': msg}


class IndexPattern(Schema):
    """ Represents an Index Pattern from Kibana/Kidash """

    # Correspondence between Schema types and panel (index pattern) types
    # There's no keyword and text types when exporting using kidash
    # We could build those by following:
    #  - If type==string and analyzed==False ==> keyword
    #  - If type==string and analyzed==True  ==> text
    # We use a dictionary defined below to match those cases
    __types = {'text': {'type': 'string', 'analyzed': True},
               'keyword': {'type': 'string', 'analyzed': False},
               'number': {'type': 'number', 'analyzed': False}}

    def __init__(self, schema_name, time_field_name):
        super().__init__(schema_name)
        self.time_field_name = time_field_name

    @classmethod
    def from_json(cls, ip_json):
        """Builds a Panel object from a Kidash panel JSON file"""

        index_pattern = cls(schema_name=ip_json['id'],
                            time_field_name=ip_json['value']['timeFieldName'])

        # Get index pattern fields
        fields_json = json.loads(ip_json['value']['fields'])
        for json_field in fields_json:
            if 'scripted' in json_field and json_field['scripted']:
                # Don't check Kibana generated scripted fields
                continue
            if not 'aggregatable' in json_field:
                logging.error('%s does not include aggregatable field. ' + \
                              'Excluded from field checking.', json_field)
                continue
            index_pattern.add_property(pname=json_field['name'],
                                       ptype=json_field['type'],
                                       analyzed=json_field['analyzed'],
                                       agg=json_field['aggregatable'])

        return index_pattern

    @staticmethod
    def get_schema_type(src_type, analyzed):
        """Type conversion from index pattern types to schema types.
        """
        out_type = src_type
        for schema_type in IndexPattern.__types:
            if src_type == IndexPattern.__types[schema_type]['type']:
                if analyzed == IndexPattern.__types[schema_type]['analyzed']:
                    out_type = schema_type

        return out_type

    def add_property(self, pname, ptype, analyzed=False, agg=False):
        """Overwrites parent method for type conversion
        """
        schema_type = self.get_schema_type(src_type=ptype, analyzed=analyzed)
        super().add_property(pname, schema_type, analyzed, agg)


class ESMapping(Schema):
    """Represents an ES Mapping"""

    __mapping_types = {'long': 'number',
                       'integer': 'number',
                       'float': 'number',
                       'double': 'number'}
    __non_aggregatables = {'text'}

    @classmethod
    def from_json(cls, index_name, mapping_json):
        """Builds a ESMapping object from an ES JSON mapping

        AttributeError -- when more than one index mapping is found in JSON
        """
        es_mapping = cls(schema_name=index_name)

        # Expect just one index mapping in json, but we don't
        # know the exact name due to the aliases:
        #    GET git/_mapping
        # Could retrieve:
        #    {
        #        "git_enriched": {
        #           "mappings": {
        #               "items": {
        #                   "dynamic_templates": [
        #                       {...}
        #                   ],
        #                   "properties": {
        #                       "Author": {
        #                           ...
        mapping_list = list(mapping_json.values())
        # if len(mapping_list) != 1:
        #    raise AttributeError("There must be only 1 index per mapping.")

        for nested_json in mapping_list:
            # nested_json = mapping_list[0]
            items = nested_json['mappings']['items']['properties'].items()
            for prop, value in items:
                # Support for nested properties:
                # "channel_purpose": {
                #   "properties": {
                #     "value": {
                #       "type": "keyword"
                #     },
                #     "creator": {
                #       "type": "keyword"
                #     },
                #     "last_set": {
                #       "type": "long"
                #     }
                #   }
                # },
                if 'properties' in value:
                    for nested_prop, nested_value in value['properties'].items():
                        prop_name = prop + '.' + nested_prop
                        analyzed = None
                        agg = None

                        if 'fielddata' in nested_value:
                            agg = nested_value['fielddata']
                        if 'type' in nested_value:
                            ptype = nested_value['type']
                        else:
                            logging.warning('Not adding to es_mapping checking ' + \
                                            'the nested value: %s', nested_value)
                            continue
                        es_mapping.add_property(pname=prop_name,
                                                ptype=ptype,
                                                analyzed=analyzed, agg=agg)

                # Support for "regular" properties
                # "channel_id": {
                #   "type": "keyword"
                # },
                else:
                    analyzed = None
                    agg = None
                    if 'fielddata' in value:
                        agg = value['fielddata']
                    es_mapping.add_property(pname=prop, ptype=value['type'],
                                            analyzed=analyzed, agg=agg)

        return es_mapping

    @staticmethod
    def get_schema_type(src_type):
        """Type conversion from ES mapping types to schema types.
        """
        out_type = src_type
        if src_type in ESMapping.__mapping_types:
            out_type = ESMapping.__mapping_types[src_type]

        return out_type

    def add_property(self, pname, ptype, analyzed=False, agg=None):
        """Overwrites parent method for type conversion
        """
        schema_type = self.get_schema_type(src_type=ptype)

        # Those fields not explicitely specified as aggregatable or not will be
        # aggregatables depending on their type
        schema_agg = agg
        if schema_agg is None:
            if schema_type in self.__non_aggregatables:
                schema_agg = False
            else:
                schema_agg = True
        super().add_property(pname, schema_type, analyzed, schema_agg)


class Panel(object):
    """ Bitergia Dashboard Panel """

    def __init__(self):
        """ Create a Panel containing a list of IndexPatterns.

        Example:
            {
                'git':
                    'time_field_name': 'grimoire_creation_date',
                    'schema_name': 'git',
                    'properties':{
                        'author_name': {
                            'type': 'text',
                            'analyzed':  true,
                            'fielddata': true
                        }
                        ...
                    }
                }
            }
        """
        self.__index_patterns = {}

    @classmethod
    def from_json(cls, panel_json):
        """Builds a Panel object from a Kidash panel JSON file"""

        panel = cls()

        index_patterns_json = panel_json['index_patterns']
        for ip_json in index_patterns_json:

            index_pattern = IndexPattern.from_json(ip_json)

            panel.add(index_pattern=index_pattern)

        return panel

    def add(self, index_pattern):
        """Add an IndexPattern object to current panel.

        Keyword arguments:
        index_pattern   -- IndexPattern instance

        """
        self.__index_patterns[index_pattern.schema_name] = index_pattern

    def get_index_pattern(self, name):
        """Returns index pattern given its name"""
        return self.__index_patterns[name]

    def get_index_patterns(self):
        """Returns Panel index patterns"""
        return self.__index_patterns
