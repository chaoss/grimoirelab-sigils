#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Bitergia
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
""" Beautify JSON panel files replacing size values as specified
"""

import argparse
import logging
import os
import sys

import utils

TO_KIBANA5_DESC_MSG = \
    """Modifies kibana 4 panel json files to import them into kibana5."""

# Logging formats
LOG_FORMAT = "[%(asctime)s] - %(message)s"
DEBUG_LOG_FORMAT = "[%(asctime)s - %(name)s - %(levelname)s] - %(message)s"

def main():
    """Read a directory containing json files for Kibana panels,
    beautify them and replace size value in aggregations as specified
    through corresponding params params.
    """
    args = parse_args()
    configure_logging(args.debug)

    src_path = args.src_path
    dest_path = args.dest_path
    old_str = '\\"size\\":' + args.old_size
    new_str = '\\"size\\":' + args.new_size

    logging.info('Input path: %s', src_path)
    logging.info('Output path: %s', dest_path)
    logging.info('old str: %s', old_str)
    logging.info('new str: %s', new_str)

    if os.path.abspath(src_path) == os.path.abspath(dest_path):
        logging.error('source and destination directiories must be different')
        sys.exit(1)

    # Iterate over input files
    json_files = [f for f in os.listdir(src_path) if f.endswith('.json')]
    for filename in json_files:

        in_file_path = os.path.join(src_path, filename)
        in_file_path = os.path.join(src_path, filename)

        out_file_path = os.path.join(dest_path, filename)
        logging.info('INPUT FILE: %s',in_file_path)
        logging.info('OUTPUT FILE: %s',out_file_path)
        # First beautify input
        pretty = utils.beautify(filename=in_file_path)

        # Iterate the beautified json string line by line
        pretty_replaced = utils.replace(pretty, old_str, new_str)

        with open(out_file_path, 'w') as output_file:
            output_file.write(pretty_replaced)

    logging.info('This is the end.')

def parse_args():
    """Parse arguments from the command line"""

    parser = argparse.ArgumentParser(description=TO_KIBANA5_DESC_MSG)

    parser.add_argument('-s', '--source', dest='src_path', \
        required=True, help='source directory')
    parser.add_argument('-d', '--dest', dest='dest_path', \
        required=True, help='destination directory')

    parser.add_argument('-o', '--old-size', dest='old_size', \
        default='0', help='aggregation old size')
    parser.add_argument('-n', '--new-size', dest='new_size', \
        default='1000', help='aggregation new size')

    parser.add_argument('-g', '--debug', dest='debug',
                        action='store_true')

    return parser.parse_args()


def configure_logging(debug=False):
    """Configure logging
    The function configures log messages. By default, log messages
    are sent to stderr. Set the parameter `debug` to activate the
    debug mode.
    :param debug: set the debug mode
    """
    if not debug:
        logging.basicConfig(level=logging.INFO,
                            format=LOG_FORMAT)
    else:
        logging.basicConfig(level=logging.DEBUG,
                            format=DEBUG_LOG_FORMAT)


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
