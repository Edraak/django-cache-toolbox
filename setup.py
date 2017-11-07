#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-cache-toolbox',
    description="Non-magical object caching for Django.",
    version='0.2.4',
    url='https://chris-lamb.co.uk/projects/django-cache-toolbox',

    author='Chris Lamb',
    author_email='chris@chris-lamb.co.uk',
    license='BSD',

    packages=find_packages(exclude=('tests',)),
    dependency_links=[
        "git+https://github.com/edx/opaque-keys.git@1254ed4d615a428591850656f39f26509b86d30a#egg=opaque-keys-0.1.2",
    ],
    install_requires=(
        "Django>=1.8",
        "opaque-keys==0.1.2",
    ),

    test_suite='tests',
)
