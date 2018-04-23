# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='solargraph-utils.py',
    version='1.1.0',
    description='solargraph-utils for python',
    long_description=readme,
    author='uplus',
    author_email='',
    url='https://github.com/uplus/solargraph-utils.py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
