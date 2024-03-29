# -*- coding: utf-8 -*-
"""City Packages component using Plone."""
from setuptools import find_packages
from setuptools import setup

import os

version = '1.0.0'

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'HISTORY.rst')) as f:
    CHANGES = f.read()

requires = [
    'Plone',
    'plone.api',
    'plone.app.contenttypes',
    'plone.app.upgrade',
    'plone.rest',
    'plone.restapi>=1.0a20',
    'requests',
    'setuptools',
    'wheel',
]

test_requirements = [
    'flake8',
    'httmock',
    'plone.app.robotframework',
    'plone.app.testing [robot] >=4.2.2',
    'plone.browserlayer',
    'plone.testing',
    'robotsuite',
]

setup(
    name='briefy.cp',
    version=version,
    description='City Packages component using Plone.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Development Status :: 5 - Production',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.1',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author='Briefy Tech Team',
    author_email='developers@briefy.co',
    url='https://github.com/BriefyHQ/briefy.cp',
    keywords='cms plone briefy',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['briefy', ],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
    install_requires=requires,
    extras_require={
        'test': test_requirements
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
