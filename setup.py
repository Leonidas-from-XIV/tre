#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Setup file for the library. This is only needed for installation"""

try:
    from setuptools import setup
    setuptools = True
except ImportError:
    from distutils.core import setup
    setuptools = False

import tre

fields = {
    'name' : 'mat-tre',
    'version' : tre.__version__,
    'description' : ('Binding to the TRE regular expression engine '
        'with approximate matching support'),
    'long_description' : open('README').read(),
    'license' : 'MIT',
    'author' : 'Marek Kubica',
    'author_email' : 'marek@xivilization.net',
    'py_modules' : ['tre'],
    'keywords' : 'regex',
    'platforms' : 'any',
    'classifiers' : [
        'License :: OSI Approved :: MIT License',
        'License :: DFSG Approved',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Filters',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ]

}

if setuptools:
    fields.update({
        'zip_safe' : True,
        'test_suite' : 'nose.collector'
    })

setup(**fields)
