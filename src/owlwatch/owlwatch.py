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


def cmp_mapping_panel(es_host, panel_path):
    """Compares ES mappings to index patterns from a given panel. Comapares
    only those mappings appearing as index patterns in JSON panel file.
    """
    return cmp_panel_mapping(panel_path, es_host, True)


def cmp_panel_mapping(panel_path, es_host, reverse=False):
    """Compares index patterns from a given panel to the corresponding
    mappings from a given ES host.

    Returns a dictionary containing tuples with status ('OK', 'ERROR')
    and message. Dictionary keys are index pattern names.

    Keyword arguments:
    es_host       -- Elastic Search host to retrieve mappings
    panel_path    -- JSON panel file path
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


def cmp_mapping_csv(es_host, csv_path):
    raise NotImplementedError('Function not implemented yet!')


def cmp_panel_csv(panel_path, csv_path):
    raise NotImplementedError('Function not implemented yet!')


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
    group_exc.add_argument('-c', '--csv-file', dest='csv_path',
                           required=False, help='Index CSV file path')


def parse_args():
    """Parse arguments from the command line"""
    parser = argparse.ArgumentParser(description=DESC_MSG,
                                     formatter_class=RawTextHelpFormatter)

    group_exc = parser.add_mutually_exclusive_group(required=False)
    group_exc.add_argument('-g', '--debug', dest='debug', action='store_true')
    group_exc.add_argument('-l', '--info', dest='info', action='store_true')

    subparsers = parser.add_subparsers(dest='subparser_name')
    add_mapping_subparser(subparsers)
    add_panel_subparser(subparsers)

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
        if csv_path is None:
            results = cmp_mapping_panel(es_host=host, panel_path=panel_path)
        elif panel_path is None:
            second = "csv"
            results = cmp_mapping_csv(es_host=host, csv_path=csv_path)

    elif args.subparser_name == CMP_PANEL:
        first = "panel"
        host = args.es_host
        panel_path = args.panel_path
        csv_path = args.csv_path
        if host is None:
            second = "csv"
            results = cmp_panel_csv(panel_path=panel_path, csv_path=csv_path)
        elif csv_path is None:
            second = "mapping"
            results = cmp_panel_mapping(panel_path=panel_path, es_host=host)

    if results is not None:
        for index_name, result in results.items():
            status = result['status']
            correct = result['correct']
            missing = result['missing']
            distinct = result['distinct']
            msg = result['msg']

            result_format = FORMAT_OK
            if status == 'OK':
                logging.info(str(correct) + "\nResult: " + status)
            else:
                result_format = FORMAT_ERROR
                logging.info(msg + "\nResult: " + status)

            print("-" * (len(index_name) + 4))
            print("* " + index_name + " *")
            print("-" * (len(index_name) + 4))
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
