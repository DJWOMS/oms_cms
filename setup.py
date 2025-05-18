#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

VERSION = "0.11.0"
RELEASE = VERSION

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
        return f.read()

def get_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name='oms-cms',
    version=VERSION,
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    description='Высокоуровневая open-source CMS на Python/Django',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='DJWOMS - Omelchenko Michael',
    author_email='socanime@gmail.com',
    url='https://github.com/DJWOMS/oms_cms',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=get_requirements('requirements/base.txt'),
    extras_require={
        'dev': get_requirements('requirements/dev.txt'),
        'prod': get_requirements('requirements/prod.txt'),
    },
    entry_points={
        'console_scripts': [
            'oms-start=oms_cms.scripts.create_project:cli_create',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://oms-cms.readthedocs.io/ru/latest/',
        'Source': 'https://github.com/DJWOMS/oms_cms',
        'Tracker': 'https://github.com/DJWOMS/oms_cms/issues',
    },
    zip_safe=False,
)
