import os

from setuptools import find_packages, setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="sound4python",
    version="0.2.0",
    author="Peter Rennert, dave.crist@gmail.com, vin985",
    author_email="p.rennert@cs.ucl.ac.uk, dave.crist@gmail.com",
    description=("comfortable playback of wav files"),
    packages=find_packages(),
    license=read('LICENSE.txt'),
    keywords="wav",
    url="https://github.com/vin985/sound4python",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
    ],
)
