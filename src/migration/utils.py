# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Bitergia
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
#   Alberto Pérez García-Plaza <alpgarcia@bitergia.com>
#

import json
import logging

def beautify(filename=None, json_str=None):
    """Beautify JSON string or file.

    Keyword arguments:
    :param filename: use its contents as json string instead of
    json_str param.
    :param json_str: json string to be beautified.
    """
    if filename is not None:
        with open(filename) as json_file:
            json_str = json.load(json_file)

    return  json.dumps(json_str, indent=4, sort_keys=True)

def replace(pretty, old_str, new_str):
    """ Replace strings giving some info on where
    the replacement was done
    """
    out_str = ''
    line_number = 1
    changes = 0
    for line in pretty.splitlines(keepends=True):
        new_line = line.replace(old_str, new_str)
        if line.find(old_str) != -1:
            logging.debug('%s', line_number)
            logging.debug('< %s', line)
            logging.debug('> %s', new_line)
            changes += 1
        out_str += new_line
        line_number += 1

    logging.info('Total changes(%s): %s', old_str, changes)
    return out_str
