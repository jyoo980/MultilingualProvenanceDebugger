#!/usr/bin/env python

from setuptools import setup

setup(name='provdebug',
    version='0.41',
    description='Multilingual Provenance Debugger',
    url='http://github.com/jwons/MultilingualProvenanceDebugger', 
    author='Joseph Wonsil',
    author_email='jwonsil@cs.ubc.ca',
    license='GPL 3.0',
    packages=['provdebug'],
    install_requires=[
        'pandas',
        'networkx',
        'numpy',
        'natsort',
        'requests'      
    ],
    entry_points = {
     'console_scripts': [
         'provdb = provdebug.pvdebug:run'
     ],
    },
    zip_safe=False)