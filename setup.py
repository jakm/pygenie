#!/usr/bin/env python
# -*- coding: utf8 -*-

from distutils.core import setup

setup(name='PyGenie',
      version='svn-r44-1',
      description='cli tool to measure complexity of python code',
      author='David Stenek',
      url='http://aufather.wordpress.com/2010/08/21/python-cyclomatic-complexity-pygenie/',
      scripts=['pygenie'],
      packages=['genie'])
