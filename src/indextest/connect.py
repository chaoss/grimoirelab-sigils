# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Daniel Izquierdo Cortazar <dizquierdo@bitergia.com>
#

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Mapping

class ESConnection(object):
    """ ElasticSearch class connection """

    def __init__(self, host='localhost', port='9200', protocol='http', path=None, user=None, password=None):
        """ Class constructor

        :param url: ElasticSearch host domain
        :param port: ElasticSearch port connection
        :param protocol: ElasticSearch protocol (typically http or https)
        :param path: ElasticSearch patch connection
        :param user: ElasticSearch user connection
        :param password: ElasticSearch password connection
        """

        credentials = ""
        if user is not None or password is not None:
            credentials = user + ":" + password + "@"
        if path is None:
            path = ""
        connection = protocol + "://" + credentials + host + ":" + port + path
        print(connection)
        self.es = Elasticsearch([connection])

    def mapping(self, index, document):
        """ This method looks for the mapping in an index for a given document type

        :param index: Elasticsearch index
        :param document: type of document

        :returns: dictionary with the mapping
        """

        mapping = Mapping.from_es(index, document, using=self.es)
        return mapping.to_dict()[document]['properties']

