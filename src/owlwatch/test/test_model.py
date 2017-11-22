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

import json
import os
import sys
import unittest

# Make sure we use our code and not any other could we have installed
sys.path.insert(0, '..')

from schema.model import ESMapping
from schema.model import IndexPattern
from schema.model import Panel


class TestPanel(unittest.TestCase):

    def setUp(self):

        self.__data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                       'data')

        # Reference properties for Git schema
        with open(os.path.join(self.__data_dir, 'git-schema_reference.json')) as f:
            self.__ref_mapping_props = json.load(f)

        # JSON mapping for git
        with open(os.path.join(self.__data_dir, 'git-mapping.json')) as f:
            self.__mapping_json = json.load(f)

        # JSON Panel for git
        with open(os.path.join(self.__data_dir, 'git.json')) as f:
            self.__panel_json = json.load(f)

        # JSON index pattern for git
        with open(os.path.join(self.__data_dir, 'git-index-pattern.json')) as f:
            self.__index_pattern_json = json.load(f)

        # Show all diferences when comparing dicts
        # (no ouput limit)
        self.maxDiff = None

    def test_index_pattern_type_text(self):
        """Test type conversion from analyzed string to text type"""
        self.assertEqual(IndexPattern.get_schema_type('string', True),
                         'text')

    def test_index_pattern_type_keyword(self):
        """Test type conversion from not analyzed string to keyword type"""
        self.assertEqual(IndexPattern.get_schema_type('string', False),
                         'keyword')

    def test_index_pattern_type_number(self):
        """Test type conversion from not analyzed number to number type"""
        self.assertEqual(IndexPattern.get_schema_type('number', False),
                         'number')

    def test_index_pattern_type_date(self):
        """Test type conversion for date type: remains unchanged"""
        self.assertEqual(IndexPattern.get_schema_type('date', False),
                         'date')
        self.assertEqual(IndexPattern.get_schema_type('date', True),
                         'date')
        self.assertEqual(IndexPattern.get_schema_type('date', None),
                         'date')

    def test_index_pattern_type_boolean(self):
        """Test type conversion for date type: remains unchanged"""
        self.assertEqual(IndexPattern.get_schema_type('boolean', False),
                         'boolean')
        self.assertEqual(IndexPattern.get_schema_type('boolean', True),
                         'boolean')
        self.assertEqual(IndexPattern.get_schema_type('boolean', None),
                         'boolean')

    def test_index_pattern_type_geo_point(self):
        """Test type conversion for date type: remains unchanged"""
        self.assertEqual(IndexPattern.get_schema_type('geo_point', False),
                         'geo_point')
        self.assertEqual(IndexPattern.get_schema_type('geo_point', True),
                         'geo_point')
        self.assertEqual(IndexPattern.get_schema_type('geo_point', None),
                         'geo_point')

    def test_index_pattern_from_json(self):
        """Test IndexPattern from_json class method"""
        index_pattern = IndexPattern.from_json(self.__index_pattern_json)

        self.assertEqual(index_pattern.time_field_name,
                         'grimoire_creation_date')
        self.assertDictEqual(index_pattern.get_properties(),
                             self.__ref_mapping_props)

    def test_es_mapping_type_text(self):
        """Test type conversion for text type: remains unchanged"""
        self.assertEqual(ESMapping.get_schema_type('text'),
                         'text')

    def test_es_mapping_type_keyword(self):
        """Test type conversion for keyword type: remains unchanged"""
        self.assertEqual(ESMapping.get_schema_type('keyword'),
                         'keyword')

    def test_es_mapping_type_long(self):
        """Test type conversion from long type to number"""
        self.assertEqual(ESMapping.get_schema_type('long'),
                         'number')

    def test_es_mapping_type_integer(self):
        """Test type conversion from integer type to number"""
        self.assertEqual(ESMapping.get_schema_type('integer'),
                         'number')

    def test_es_mapping_type_float(self):
        """Test type conversion from float type to number"""
        self.assertEqual(ESMapping.get_schema_type('float'),
                         'number')

    def test_es_mapping_type_double(self):
        """Test type conversion from double type to number"""
        self.assertEqual(ESMapping.get_schema_type('double'),
                         'number')

    def test_es_mapping_type_date(self):
        """Test type conversion for date type: remains unchanged"""
        self.assertEqual(ESMapping.get_schema_type('date'),
                         'date')

    def test_es_mapping_type_boolean(self):
        """Test type conversion for boolean type: remains unchanged"""
        self.assertEqual(ESMapping.get_schema_type('boolean'),
                         'boolean')

    def test_es_mapping_type_geo_point(self):
        """Test type conversion for geo_point type: remains unchanged"""
        self.assertEqual(ESMapping.get_schema_type('geo_point'),
                         'geo_point')

    def test_es_mapping_from_json(self):
        """Test ESMapping from_json class method"""
        es_mapping = ESMapping.from_json(index_name='git',
                                         mapping_json=self.__mapping_json)

        self.assertDictEqual(es_mapping.get_properties(),
                             self.__ref_mapping_props)

    def test_panel_from_json(self):
        """Test Panel from_json class method"""
        panel = Panel.from_json(self.__panel_json)

        self.assertEqual(len(panel.get_index_patterns()), 1)
        self.assertEqual(panel.get_index_pattern('git').time_field_name,
                         'grimoire_creation_date')
        self.assertDictEqual(panel.get_index_pattern('git').get_properties(),
                             self.__ref_mapping_props)

    def test_schema_compare_equal(self):
        """Test comparison between Schema properties using its
        compare method"""

        expected_status = 'OK'

        # Check comparison against the same object
        es_mapping = ESMapping.from_json(index_name='git',
                                         mapping_json=self.__mapping_json)

        # ESMapping vs ESMapping
        result = es_mapping.compare_properties(es_mapping)
        self.assertEqual(result['status'], expected_status)
        self.assertEqual(result['correct'], list(es_mapping.get_properties().keys()))

        # Check comparison ESMapping vs IndexPattern
        index_pattern = IndexPattern.from_json(self.__index_pattern_json)

        result = es_mapping.compare_properties(index_pattern)
        self.assertEqual(result['status'], expected_status)
        self.assertEqual(result['correct'], list(es_mapping.get_properties().keys()))

        # Check comparison IndexPattern vs ESMapping
        result = index_pattern.compare_properties(es_mapping)
        self.assertEqual(result['status'], expected_status)
        self.assertEqual(result['correct'], list(index_pattern.get_properties().keys()))

        #
        # Second schema could have more properties than
        # first one (used to COMPARE FROM it)
        # Add a new property to this second instance
        #

        es_mapping_mod = ESMapping.from_json(index_name='git',
                                             mapping_json=self.__mapping_json)
        es_mapping_mod.get_properties()['fake_prop'] = 0

        # Mapping vs Mapping
        result = es_mapping.compare_properties(es_mapping_mod)
        self.assertEqual(result['status'], expected_status)

        # Index pattern vs Mapping
        result = index_pattern.compare_properties(es_mapping_mod)
        self.assertEqual(result['status'], expected_status)

    def test_schema_compare_distinct(self):
        """Test comparison between Schema properties using its
        compare method"""
        expected_status = 'KO'

        # Check comaprison against the same object slightly modified
        es_mapping = ESMapping.from_json(index_name='git',
                                         mapping_json=self.__mapping_json)

        es_mapping_mod = ESMapping.from_json(index_name='git',
                                             mapping_json=self.__mapping_json)

        #
        # Add fake property to the schema used to COMPARE FROM
        #

        es_mapping_mod.get_properties()['fake_prop'] = 'text'

        # ESMapping vs ESMapping
        result = es_mapping_mod.compare_properties(es_mapping)
        self.assertEqual(result['status'], expected_status)
        self.assertEqual(result['missing'], ['fake_prop'])

        # Check comparison ESMapping vs IndexPattern
        index_pattern = IndexPattern.from_json(self.__index_pattern_json)

        result = es_mapping_mod.compare_properties(index_pattern)
        self.assertEqual(result['status'], expected_status)
        self.assertEqual(result['missing'], ['fake_prop'])

        #
        # Add fake property to the target schemas with different value
        #

        es_mapping.add_property('fake_prop', 'text')
        index_pattern.add_property('fake_prop', 'text')

        # ESMapping vs ESMapping
        result = es_mapping_mod.compare_properties(es_mapping)
        self.assertEqual(result['status'], expected_status)
        self.assertEqual(result['missing'], [])
        self.assertEqual(result['distinct'], ['fake_prop'])

        # Check comparison ESMapping vs IndexPattern
        result = es_mapping_mod.compare_properties(index_pattern)
        self.assertEqual(result['status'], expected_status)
        self.assertEqual(result['missing'], [])
        self.assertEqual(result['distinct'], ['fake_prop'])

    def test_schema_compare_last_item(self):
        """Test comparison between Schema properties using its
        compare method with the last item different (but the same fields)"""

        expected_status = 'OK'

        mapping_json = None
        panel_json = None

        # Mapping for git enrich loaded from mordred
        with open(os.path.join(self.__data_dir,
                               'git-mapping-utc_commit.json')) as fjson:
            mapping_json = json.load(fjson)

        # JSON Panel for git
        with open(os.path.join(self.__data_dir, 'git-utc_commit.json')) as fjson:
            panel_json = json.load(fjson)

        # Check comaprison against the same object slightly modified
        es_mapping = ESMapping.from_json(index_name='git_test',
                                         mapping_json=mapping_json)
        panel = Panel.from_json(panel_json)

        result = panel.get_index_pattern('git').compare_properties(es_mapping)

        if result['status'] != expected_status:
            print(result)

        self.assertEqual(result['status'], expected_status)


if __name__ == '__main__':
    unittest.main()
