#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

SCRIPTDIR = path.abspath(path.dirname(__file__))

with open(path.join(SCRIPTDIR, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
                             name = "getopts",
                      description = "A classic getopt library with long options and optional arguments support.",
                          version = "1.0.5",
                          license = "Apache 2.0",
                           author = "Mark Kim",
                     author_email = "markuskimius+py@gmail.com",
                              url = "https://github.com/markuskimius/getopt-py",
                         keywords = [ "getopt" ],
                 long_description = long_description,
    long_description_content_type = "text/markdown",
                         packages = find_packages("src"),
                      package_dir = { "": "src" },
)
