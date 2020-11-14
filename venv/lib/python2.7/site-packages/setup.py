import os
import sys
from setuptools import setup

# Use a cute trick to include the rest-style docs as the long_description
# therefore having it self-doc'ed and hosted on pypi
with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='pyjavaproperties',
    version='0.7',
    author='Anand B Pillai',
    author_email = 'anandpillai@letterboxes.org',
    description = 'Python replacement for java.util.Properties.',
    long_description = long_description,
    url='https://bitbucket.org/skeptichacker/pyjavaproperties/',
    
    license = 'MIT License',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
    py_modules=['pyjavaproperties'],
    packages=[''],
    package_dir={'': '.'},
    )
