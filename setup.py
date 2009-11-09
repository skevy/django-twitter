#!/usr/bin/env python
# django-twitter -  Twitter integration for django
# 
# Copyright (C) 2009 Adam Miskiewicz
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""Twitter integration for django

A django app that allows for django and twitter integration
"""

from distutils.core import setup


description, long_description = __doc__.split('\n\n', 1)
VERSION = '0.1'

setup(
    name='django-twitter',
    version=VERSION,
    author='Adam Miskiewicz',
    author_email='adam@sk3vy.com',
    description=description,
    long_description=long_description,
    license='BSD',
    platforms=['any'],
    url='http://github.com/skevy/django-twitter/',
    packages=[
        'django_twitter',
        ],
    provides=['django_twitter'],
    requires=['django (>=1.1)', 'simplejson', 'django_bitly'],
    )
