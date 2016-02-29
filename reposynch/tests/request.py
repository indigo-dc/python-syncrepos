#!/usr/bin/env python

# Copyright 2016, Atos Spain SA.                                             #
# Author: Jorge Edgar Valderrama Romero
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
# Copyright 2011 OpenStack, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
from reposynch import  api

api_data= {"push_data": {	"pushed_at": 1456748821,"images": [],"tag": "latest","pusher": "joedval"},
       "callback_url": "https://registry.hub.docker.com/u/joedval/indigo/hook/2eh1i0cd2j4gb4i5heii2ccfeehf52ic3/",
       "repository": {	"status": "Active",
                          "description": "Repo test for OpenNebula and OpenStack synchronization images",
                          "is_trusted": 'false',
                          "full_description": "",
                          "repo_url": "https://registry.hub.docker.com/u/joedval/indigo/",
                          "owner": "joedval",
                          "is_official": 'false',
                          "is_private": 'false',
                          "name": "indigo",
                          "namespace": "joedval",
                          "star_count": 0,
                          "comment_count": 0,
                          "date_created": 1456481821,
                          "repo_name": "joedval/indigo"}}
r = requests.post(api.target_url, data=api_data)
print r.status_code
print r.content