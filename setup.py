#! /usr/bin/env python
#
# Copyright (C) 2018 Mikko Kotila

import os

DESCRIPTION = "Signs Text Processing for Deep Learning"
LONG_DESCRIPTION = """\
Signs is a utility for text preprocessing, vectorizing, and analysis
such as semantic similarity, mainly for the purpose of using unstructured
data in deep learning models.
"""

DISTNAME = 'signs'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://autonom.io'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/autonomio/signs/'
VERSION = '0.3.2'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

install_requires = ['kerasplotlib',
                    'wrangle',
                    'pandas',
                    'numpy',
                    'cython',
                    'spacy',
                    'gensim',
                    'keras',
                    'ipython']

if __name__ == "__main__":

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['signs',
                    'signs.commands',
                    'signs.preprocess',
                    'signs.vectorize',
                    'signs.grams',
                    'signs.utils',
                    'signs.models',
                    'signs.similarity'],

          classifiers=[
                'Intended Audience :: Science/Research',
                'Programming Language :: Python :: 3.6',
                'License :: OSI Approved :: MIT License',
                'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                'Topic :: Scientific/Engineering :: Artificial Intelligence',
                'Topic :: Scientific/Engineering :: Mathematics',
                'Operating System :: POSIX',
                'Operating System :: Unix',
                'Operating System :: MacOS'])

os.system("python -m spacy download en")
