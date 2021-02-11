# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in erpnext/__init__.py
version = "1.0.0"

setup(
	name='kis',
	version=version,
	description='Open Source ERP',
	author='Frappe Technologies',
	author_email='info@erpnext.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=("frappe",),
)
