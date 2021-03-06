#!/usr/bin/env python

#-------------------------------------------------------------------------
# Copyright (c) Microsoft.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#--------------------------------------------------------------------------

from distutils.core import setup

setup(name='ptvsd',
      version='2.2.0rc2',
      description='Python Tools for Visual Studio remote debugging server',
      license='Apache License 2.0',
      author='Microsoft Corporation',
      author_email='ptvshelp@microsoft.com',
      url='https://aka.ms/ptvs',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License'],
      packages=['ptvsd']
     )
