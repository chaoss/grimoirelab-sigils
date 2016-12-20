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
#     Daniel Izquierdo Cortazar <dizquierdo@bitergia.com>
#

def compare(dictA, dictB):
    """ This function compares dictionary A and B and returns the difference

    :param dictA: dictionary of values
    :param dictB: dictionary of values

    :returns: dictionary of three entries with the result of the comparison
        * left: fields in dictA, but not in dictB.
        * right: fields in dictB, but not in dictA.
        * intersection: fields in dictA and dictB.
    :rtype: dictionary
    """

    setA_keys = set(dictA.keys())
    setB_keys = set(dictB.keys())

    listA_notinB = list(setA_keys.difference(setB_keys))
    listB_notinA = list(setB_keys.difference(setA_keys))
    intersection = list(setA_keys.intersection(setB_keys))
    result = {'left':listA_notinB,
              'right':listB_notinA,
              'intersection':intersection}

    return result

