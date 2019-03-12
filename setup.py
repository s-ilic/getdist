#!/usr/bin/env python

from __future__ import absolute_import
import io
import re
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def find_version():
    version_file = io.open(os.path.join(os.path.dirname(__file__), 'my_getdist/__init__.py')).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def get_long_description():
    with open('README.rst') as f:
        lines = f.readlines()
        i = -1
        while not '=====' in lines[i]: i -= 1
        return "".join(lines[:i])


setup(name='GetDist',
      version=find_version(),
      description='GetDist Monte Carlo sample analysis, plotting and GUI',
      long_description=get_long_description(),
      author='Antony Lewis',
      url="https://github.com/cmbant/my_getdist",
      packages=['my_getdist', 'my_getdist.gui', 'paramgrid', 'my_getdist_tests'],
      scripts=['GetDist.py', 'GetDistGUI.py'],
      test_suite='my_getdist_tests',
      package_data={'my_getdist': ['analysis_defaults.ini', 'distparam_template.ini']},
      install_requires=[
          'packaging',
          'numpy',
          'matplotlib',
          'six',
          "scipy (>=0.11.0)"],
      # PySide or pyside2 is needed for the GUI
      #  optional (for faster file read)
      # 'pandas (>=0.14.0)'
      classifiers=[
          "Programming Language :: Python :: 2",
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      keywords=['MCMC', 'KDE', 'sample', 'density estimation', 'plot']
      )
