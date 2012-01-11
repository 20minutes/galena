# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='galena',
    version='0.3',
    description='Dumb but useful graphite/carbon client.',
    author='Timothée Peignier',
    author_email='tpeignier@20minutes.fr',
    url='https://github.com/20minutes/galena',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    test_suite='galena.tests',
    tests_require=['mock'],
    classifiers=[
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
