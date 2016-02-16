#!/usr/bin/env python

# Copyright 2016, Atos Spain SA.                                             #
# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
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

import os
import setuptools

from reposynch import setup

requires = setup.parse_requirements()
depend_links = setup.parse_dependency_links()
tests_require = setup.parse_requirements(['test-requirements.txt'])
project = 'python-reposynch'


def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setuptools.setup(
    name=project,
    # version=setup.get_version(project),
    version="1.0",
    author="Jorge Valderrama Romero",
    author_email="jorge.valderrama@atos.net",
    description="RepoSynch is a lightweight API to synchronize images from Docker Hub in OpenStack and OpenNebula "
                "Platforms",
    long_description=read_file("README.rst"),
    license="Apache License, Version 2.0",
    url="https://github.com/jvalderrama/python-syncrepos",
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    cmdclass=setup.get_cmdclass(),
    install_requires=requires,
    tests_require=tests_require,
    setup_requires=['setuptools-git>=0.4'],
    include_package_data=True,
    dependency_links=depend_links,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: System"
    ]
)
