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
#     Daniel Izquierdo <dizquierdo@bitergia.com>
#

import sys

import unittest


if not '..' in sys.path:
    sys.path.insert(0, '..')

import json2csv

class TestFormat(unittest.TestCase):
    """ Unit test for the format
    """

    def test_json2tuple(self):
        """ Test several cases about the input format
        """

        output = json2csv.json2tuple('data/test_short.json')
        print (output)
        self.assertEqual(output, [("author","text")])


if __name__ == '__main__':
    unittest.main()
