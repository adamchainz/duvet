#/usr/bin/env python
import sys

from setuptools import setup
from duvet import VERSION

try:
    readme = open('README.rst')
    long_description = str(readme.read())
finally:
    readme.close()

required_pkgs = []
if sys.version_info < (2, 7):
    required_pkgs.append('argparse')

setup(
    name='duvet',
    version=VERSION,
    description='GUI tool for visualizing code coverage results.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/duvet',
    packages=[
        'duvet',
    ],
    install_requires=required_pkgs,
    scripts=['scripts/duvet'],
    license='New BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    test_suite='tests'
)