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

from bottle import post, request, HTTPError, run, response
from config import Config
import logging
import json
import os
import datetime

now = datetime.datetime.now()

# curl -i -H \"Accept: application/json\" -H \"Content-Type: application/json\" -X POST -d "{\"callback_url\":
# \"https://registry.hub.docker.com/u/svendowideit/busybox/hook/2141bc0cdec4hebec411i4c1g40242eg110020/\",
# \"push_data\": {\"images\": [\"27d47432a69bca5f2700e4dff7de0388ed65f9d3fb1ec645e2bc24c223dc1cc3\",
# \"51a9c7c1f8bb2fa19bcd09789a34e63f35abb80044bc10196e304f6634cc582c\"],\"pushed_at\": 1.417566822e+09,\"pusher\":
# \"svendowideit\"},\"repository\": {\"comment_count\": 0,\"date_created\": 1.417566665e+09,\"description\": \"\",
# \"full_description\": \"webhook triggered from a 'docker push'\",\"is_official\": false,\"is_private\":
# false,\"is_trusted\": false,\"name\": \"busybox\",\"namespace\": \"svendowideit\",\"owner\": \"svendowideit\",
# \"repo_name\": \"svendowideit/busybox\",\"repo_url\": \"https://registry.hub.docker.com/u/svendowideit/busybox/\",
# \"star_count\": 0,\"status\": \"Active\"}" http://localhost:8080/synch -v
@post('/synch')
def sync_repo():
    try:
        #print request.body.read()
        log_filename = 'reposynch.log'
        logging.basicConfig(filename=log_filename,level=logging.INFO)
        if  os.system('dpkg -l|grep opennebula')== 0:
            logging.info(' {} : OpenNebula has been detected as Cloud Provider ...'.
                         format(str(now.strftime("%Y-%m-%d %H:%M"))))
            update_one(request)
            msg = 'Synchronized OpenNebula onedock datastore with Docker Hub repository'
        elif os.system('dpkg -l|grep openstack') == 0 :
            logging.info(' {} : OpenStack has been detected as Cloud Provider ...'.
                         format(str(now.strftime("%Y-%m-%d %H:%M"))))
            update_ostack(request)
            msg = 'Synchronized OpenStack glance with Docker Hub repository'
        else:
            msg = 'Something is wrong, the API was not able to detect the cloud provider ...'
            logging.error(msg.format(str(now.strftime("%Y-%m-%d %H:%M"))))
            raise Exception(msg)
        result = {'state': 'success', 'description': msg,'context': 'reposynch',
        'target_url': target_url }
        response.content_type = 'application/json'
        return json.dumps(result)
    except Exception, e:
        logging.error(e.message.format(str(now.strftime("%Y-%m-%d %H:%M"))))
        response.content_type = 'application/json'
        error = {'state': 'error', 'description': e.message,'context': 'reposynch',
        'target_url': target_url }
        return json.dumps(error)


def update_one(request):
    #TODO-Create template per image:tag, look for the current images in onedock datastore, if the image exists does not
    #TODO-do anything, otherwise create template in a specific folder to keep track of all updates and create new
    #TODO-image in ONE
    os.system('ls')


def update_ostack(request):
    #TODO-Research how is it in glance
    os.system('ls')



def init():
    path = os.path.dirname(os.path.abspath(__file__))
    f = file('%s/reposynch.cfg' %path)
    cfg = Config(f)
    global target_url
    target_url = 'http://%s:%s/synch' %(cfg.api_endpoint, cfg.api_port)
    run(host=cfg.api_endpoint, port=cfg.api_port)

if __name__ == "__main__":
    init()





