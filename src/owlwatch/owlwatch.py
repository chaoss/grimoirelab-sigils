#!/usr/bin/env python3
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

import argparse
import json
import logging
import sys

from argparse import RawTextHelpFormatter
from colorama import Fore, Style
from elasticsearch import Elasticsearch

from schema.model import ESMapping
from schema.model import Panel


DESC_MSG = \
    """
     _____________________________
    ( Who watches the dashboards? )
    ( I do.                       )
     -----------------------------
          o   -._   _.-
           o   (0),(0)
                (   )
              __.._..__Bitergia"""

# Logging formats
LOG_FORMAT = "[%(asctime)s - %(levelname)s] - %(message)s"
DEBUG_LOG_FORMAT = "[%(asctime)s - %(name)s - %(levelname)s] - %(message)s"

FORMAT_OK = Fore.GREEN
FORMAT_WARN = Fore.YELLOW
FORMAT_ERROR = Fore.RED

CMP_MAPPING = 'compare-mapping'
CMP_PANEL = 'compare-panel'
CMP_CSV = 'compare-csv'

VERSION = '0.2'


def cmp_mapping_panel(es_host, panel_path):
    """Compares ES mappings to index patterns from a given panel. Compares
    only those mappings appearing as index patterns in JSON panel file.

    Returns a dictionary where each 1st level key is an index pattern name.
    Each of these keys contains a tuple with:
        {status, correct, missing, distinct, message}
    being:
        status 'OK' if all properties in source schema exist in target
            schema with same values. 'KO' in other case.
        correct: list of properties that matches.
        missing: list of properties missing from target schema.
        distinct: list of properties in both schemas but having
            with different values.
        message: a string with additional information.

    Keyword arguments:
    es_host       -- Elastic Search host to retrieve mappings
    panel_path    -- JSON panel file path
    """
    return cmp_panel_mapping(panel_path, es_host, True)


def cmp_panel_mapping(panel_path, es_host, reverse=False):
    """Compares index patterns from a given panel to the corresponding
    mappings from a given ES host.

    Returns a dictionary where each 1st level key is an index pattern name.
    Each of these keys contains a tuple with:
        {status, correct, missing, distinct, message}
    being:
        status 'OK' if all properties in source schema exist in target
            schema with same values. 'KO' in other case.
        correct: list of properties that matches.
        missing: list of properties missing from target schema.
        distinct: list of properties in both schemas but having
            with different values.
        message: a string with additional information.

    Keyword arguments:
    panel_path    -- JSON panel file path
    es_host       -- Elastic Search host to retrieve mappings
    reverse       -- use mapping as source schema.
    """
    client = Elasticsearch(es_host, timeout=30)

    with open(panel_path) as f:
        panel_json = json.load(f)

    panel = Panel.from_json(panel_json)

    result = {}
    for index_pattern in panel.get_index_patterns().values():
        mapping_json = client.indices.get_mapping(index=index_pattern.schema_name)
        es_mapping = ESMapping.from_json(index_name=index_pattern.schema_name,
                                         mapping_json=mapping_json)
        if reverse:
            result[index_pattern.schema_name] = es_mapping.compare_properties(index_pattern)
        else:
            result[index_pattern.schema_name] = index_pattern.compare_properties(es_mapping)

    return result


def cmp_csv_mapping(csv_path, es_host):
    """Compares CSV schema definition to a given ES Mapping.

    Returns a dictionary where each 1st level key is an index pattern name.
    Each of these keys contains a tuple with:
        {status, correct, missing, distinct, message}
    being:
        status 'OK' if all properties in source schema exist in target
            schema with same values. 'KO' in other case.
        correct: list of properties that matches.
        missing: list of properties missing from target schema.
        distinct: list of properties in both schemas but having
            with different values.
        message: a string with additional information.

    Keyword arguments:
    csv_path        -- CSV schema definition file path
    es_host         -- Elastic Search host to retrieve mappings
    """
    return cmp_mapping_csv(es_host, csv_path, True)


def cmp_mapping_csv(es_host, csv_path, reverse=False):
    """Compares an ES Mapping to a given CSV schema definition.

    Returns a dictionary where each 1st level key is an index pattern name.
    Each of these keys contains a tuple with:
        {status, correct, missing, distinct, message}
    being:
        status 'OK' if all properties in source schema exist in target
            schema with same values. 'KO' in other case.
        correct: list of properties that matches.
        missing: list of properties missing from target schema.
        distinct: list of properties in both schemas but having
            with different values.
        message: a string with additional information.

    Keyword arguments:
    es_host         -- Elastic Search host to retrieve mappings
    csv_path        -- CSV schema definition file path
    reverse         -- use CSV as source schema.
    """
    # Use file name as index name
    if '/' in csv_path:
        schema_name = csv_path[csv_path.rindex('/') + 1:csv_path.rindex('.csv')]
    else:
        schema_name = csv_path[:csv_path.rindex('.csv')]

    csv_mapping = ESMapping.from_csv(index_name=schema_name,
                                     csv_file=csv_path)

    client = Elasticsearch(es_host, timeout=30)
    mapping_json = client.indices.get_mapping(index=schema_name)
    es_mapping = ESMapping.from_json(index_name=schema_name,
                                     mapping_json=mapping_json)

    result = {}

    if reverse:
        result[schema_name] = csv_mapping.compare_properties(es_mapping)
    else:
        result[schema_name] = es_mapping.compare_properties(csv_mapping)

    return result


def cmp_csv_panel(csv_path_list, panel_path):
    """Compares a list of CSV schema definitions to the corresponding
    index patterns from a given panel. Compares only those mappings appearing
    as index patterns in JSON panel file.

    Returns a dictionary where each 1st level key is an index pattern name.
    Each of these keys contains a tuple with:
        {status, correct, missing, distinct, message}
    being:
        status 'OK' if all properties in source schema exist in target
            schema with same values. 'KO' in other case.
        correct: list of properties that matches.
        missing: list of properties missing from target schema.
        distinct: list of properties in both schemas but having
            with different values.
        message: a string with additional information.

    Keyword arguments:
    csv_path_list   -- CSV schema definition file paths
    panel_path      -- JSON panel file path
    """
    return cmp_panel_csv(panel_path, csv_path_list, True)


def cmp_panel_csv(panel_path, csv_path_list, reverse=False):
    """Compares index patterns from a given panel to the corresponding
    mappings from a given CSV schema definition.

    Returns a dictionary where each 1st level key is an index pattern name.
    Each of these keys contains a tuple with:
        {status, correct, missing, distinct, message}
    being:
        status 'OK' if all properties in source schema exist in target
            schema with same values. 'KO' in other case.
        correct: list of properties that matches.
        missing: list of properties missing from target schema.
        distinct: list of properties in both schemas but having
            with different values.
        message: a string with additional information.

    Keyword arguments:
    panel_path      -- JSON panel file path
    csv_path_list   -- CSV schema definition file paths
    reverse         -- use CSV as source schema.
    """
    with open(panel_path) as f:
        panel_json = json.load(f)

    panel = Panel.from_json(panel_json)

    mappings = {}
    for csv_path in csv_path_list:
        # Use file name as index name
        if '/' in csv_path:
            schema_name = csv_path[csv_path.rindex('/') + 1:csv_path.rindex('.csv')]
        else:
            schema_name = csv_path[:csv_path.rindex('.csv')]

        mappings[schema_name] = ESMapping.from_csv(index_name=schema_name,
                                                   csv_file=csv_path)

    result = {}
    for index_pattern in panel.get_index_patterns().values():

        es_mapping = mappings[index_pattern.schema_name]

        if reverse:
            result[index_pattern.schema_name] = es_mapping.compare_properties(index_pattern)
        else:
            result[index_pattern.schema_name] = index_pattern.compare_properties(es_mapping)

    return result


def add_mapping_subparser(subparsers):
    """Adds a subparser for comparing mappings against panels or CSV
    index definitions"""
    help_txt = \
        """Compares a mapping against panel JSON file or CSV
        index definition"""
    parser_cmp = subparsers.add_parser(CMP_MAPPING,
                                       help=help_txt)

    parser_cmp.add_argument('-e', '--elastic-search', dest='es_host',
                            required=True, help='ES host')

    group_exc = parser_cmp.add_mutually_exclusive_group(required=True)
    group_exc.add_argument('-p', '--panel-file', dest='panel_path',
                           required=False, help='Panel JSON file path')
    group_exc.add_argument('-c', '--csv-file', dest='csv_path',
                           required=False, help='Index CSV file path')


def add_panel_subparser(subparsers):
    """Adds a subparser for comparing panels against ES index mapping or
    CSV index definitions"""
    help_txt = \
        """Compares a panel JSON file against a ES mapping or a
        CSV index definition"""
    parser_cmp = subparsers.add_parser(CMP_PANEL,
                                       help=help_txt)

    parser_cmp.add_argument('-p', '--panel-file', dest='panel_path',
                            required=True, help='Panel JSON file path')
    group_exc = parser_cmp.add_mutually_exclusive_group(required=True)
    group_exc.add_argument('-e', '--elastic-search', dest='es_host',
                           required=False, help='ES host')
    group_exc.add_argument('-c', '--csv-file', dest='csv_path_list',
                           action='append',
                           required=False,
                           help='Index CSV file path. Add this ' +
                           'argument as many times as CSV files you need to ' +
                           ' check.')


def add_csv_subparser(subparsers):
    """Adds a subparser for comparing CSV schema definitions against ES
    index mapping or panel JSON files"""
    help_txt = \
        """Compares a CSV index definition file against a ES mapping or a
        JSON panel"""
    parser_cmp = subparsers.add_parser(CMP_CSV,
                                       help=help_txt)

    parser_cmp.add_argument('-c', '--csv-file', dest='csv_path_list',
                            action='append',
                            required=True,
                            help='Index CSV file path. Add this ' +
                            'argument as many times as CSV files you need to ' +
                            ' check.')

    group_exc = parser_cmp.add_mutually_exclusive_group(required=True)
    group_exc.add_argument('-e', '--elastic-search', dest='es_host',
                           required=False, help='ES host')
    group_exc.add_argument('-p', '--panel-file', dest='panel_path',
                           required=False, help='Panel JSON file path')


def parse_args():
    """Parse arguments from the command line"""
    parser = argparse.ArgumentParser(description=DESC_MSG,
                                     formatter_class=RawTextHelpFormatter)

    group_exc = parser.add_mutually_exclusive_group(required=False)
    group_exc.add_argument('-g', '--debug', dest='debug', action='store_true')
    group_exc.add_argument('-l', '--info', dest='info', action='store_true')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + VERSION)

    subparsers = parser.add_subparsers(dest='subparser_name')
    add_mapping_subparser(subparsers)
    add_panel_subparser(subparsers)
    add_csv_subparser(subparsers)

    return parser.parse_args()


def configure_logging(info=False, debug=False):
    """Configure logging
    The function configures log messages. By default, log messages
    are sent to stderr. Set the parameter `debug` to activate the
    debug mode.
    :param debug: set the debug mode
    """
    if info:
        logging.basicConfig(level=logging.INFO,
                            format=LOG_FORMAT)
        logging.getLogger('requests').setLevel(logging.WARNING)
        logging.getLogger('urrlib3').setLevel(logging.WARNING)
        logging.getLogger('elasticsearch').setLevel(logging.WARNING)
    elif debug:
        logging.basicConfig(level=logging.DEBUG,
                            format=DEBUG_LOG_FORMAT)
    else:
        logging.basicConfig(level=logging.WARNING,
                            format=LOG_FORMAT)
        logging.getLogger('requests').setLevel(logging.WARNING)
        logging.getLogger('urrlib3').setLevel(logging.WARNING)
        logging.getLogger('elasticsearch').setLevel(logging.WARNING)


def main():
    """This is the Owlcave, where everything starts"""
    args = parse_args()

    configure_logging(args.info, args.debug)

    logging.info("** The Owl is watching **")

    results = None
    first = "mapping"
    second = "panel"
    if args.subparser_name == CMP_MAPPING:
        host = args.es_host
        panel_path = args.panel_path
        csv_path = args.csv_path
        logging.info("Compare Mapping from " + host)
        if csv_path is None:
            logging.info("Against Panel from " + panel_path)
            results = cmp_mapping_panel(es_host=host, panel_path=panel_path)
        elif panel_path is None:
            logging.info("Against CSV from " + csv_path)
            second = "csv"
            results = cmp_mapping_csv(es_host=host, csv_path=csv_path)

    elif args.subparser_name == CMP_PANEL:
        first = "panel"
        host = args.es_host
        panel_path = args.panel_path
        csv_path_list = args.csv_path_list
        logging.info("Compare Panel from " + panel_path)
        if host is None:
            logging.info("Against CSVs from " + str(csv_path_list))
            second = "csv"
            results = cmp_panel_csv(panel_path=panel_path,
                                    csv_path_list=csv_path_list)
        elif csv_path_list is None:
            logging.info("Against Mappings from " + host)
            second = "mapping"
            results = cmp_panel_mapping(panel_path=panel_path, es_host=host)

    elif args.subparser_name == CMP_CSV:
        first = "csv"
        host = args.es_host
        panel_path = args.panel_path
        csv_path_list = args.csv_path_list
        logging.info("Compare CSVs from " + str(csv_path_list))
        if host is None:
            logging.info("Against Panel from " + panel_path)
            second = "panel"
            results = cmp_csv_panel(csv_path_list=csv_path_list,
                                    panel_path=panel_path)
        elif panel_path is None:
            logging.info("Against Mappings from " + host)
            second = "mapping"
            results = {}
            for csv_path in csv_path_list:
                index_name, result = cmp_csv_mapping(csv_path=csv_path,
                                                     es_host=host).popitem()
                results[index_name] = result

    if results is not None:
        for index_name, result in results.items():
            status = result['status']
            correct = result['correct']
            missing = result['missing']
            distinct = result['distinct']
            msg = result['msg']

            result_format = FORMAT_OK
            if status == 'OK':
                logging.info("Matches: " + str(correct))
                logging.info("Result: " + status)
            else:
                result_format = FORMAT_ERROR
                logging.info(msg + "\nResult: " + status)

            print("-" * (len(index_name) + 4))
            print("* " + index_name + " *")
            print("-" * (len(index_name) + 4))
            print(first + " Vs. " + second)
            print("Comparison result: " + result_format + status + Style.RESET_ALL)
            print("Matches:", len(correct))
            print("Not found in " + second + ": ", len(missing))
            print("Type mismatches: ", len(distinct))
            if msg != "":
                print("Details: \n" + msg + '\n')
    else:
        logging.info("Didn't find anything to do...")

    logging.info("This is the end.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        s = "\n\nReceived Ctrl-C or other break signal. Exiting.\n"
        sys.stdout.write(s)
        sys.exit(0)
    except RuntimeError as e:
        s = "Error: %s\n" % str(e)
        sys.stderr.write(s)
        sys.exit(1)
