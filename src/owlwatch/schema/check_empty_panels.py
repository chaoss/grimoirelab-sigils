#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Bitergia
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
#     David Pose Fernández <dpose@bitergia.com>
#


import subprocess
import os
import requests

class CheckEmptyPanels:

    def get_containers(self, storage_dir):
        """
        Function to get the list of ES instances running on the host.

        :param storage_dir: directory where the containers can be found on the host.

        :returns: dict of projects and the port of their ES instances
        """
        if os.path.isdir(storage_dir):
            projects = [ x for x in os.listdir(storage_dir) if os.path.isdir(os.path.join(storage_dir, x)) ]
            containers = {}
            query = 'docker ps --format "table {{.Names}}\t{{.Ports}}" | grep _elasticsearch | grep '
            for project in projects:
                p, err = subprocess.Popen(query + project, shell=True,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE
                                         ).communicate()
                if p:
                    p_name =  (p.decode('utf-8').strip()).split("_")[0]
                    p_port =  (p.decode('utf-8').split(":")[1]).split("-")[0]
                    containers[p_name] = p_port

            return containers
        else:
            raise Exception("NotValidPath")

    def check_panel(self, panel_name, project, port=80, check_all=False, user=None, password=None):
        """
        Function to check whether a certain panel is empty or not.

        :param project: url of the ES instance of the project to be checked
        :param port: port where the ES instance is listening to
        """
        query_url = '/.kibana/_search?type=dashboard&size=10000'
        if check_all == True:
            url = 'http://localhost:' + str(port)
        elif project.rfind('http') == 0 or project.rfind('https') == 0:
            url = project + ":" + str(port)
        else:
            url = 'https://' + project + '.biterg.io/data'
        result = requests.get(url + query_url, auth=(user, password))
        result_json = result.json()

        for hit in result_json['hits']['hits']:
            if hit['_source']['title'] == panel_name:
                if hit['_source']['panelsJSON'] == "[]":
                    check = "Panel " + panel_name + " is EMPTY for " + project
                    return check
                else:
                    check = "Panel " + panel_name + " is OK for " + project
                    return check
