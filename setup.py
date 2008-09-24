#!/usr/bin/env python
# -*- coding: UTF-8 -*-
try:
    from setuptools import setup
    setuptools = True
except ImportError:
    from distutils.core import setup
    setuptools = False

import tre

fields = {
    # beware, the name is not final
    'name' : 'TRE',
    # fails deliberately to stop people from uploading to the cheese shop
    'version' : tre.__version__,
    'description' : 'Binding to the TRE regular expression engine',
    'author' : 'Marek Kubica',
    'author_email' : 'marek@xivilization.net',
    'py_modules' : ['tre']
}

if setuptools:
    fields.update({
        'zip_safe' : True,
        'test_suite' : 'nose.collector'
    })

setup(**fields)
