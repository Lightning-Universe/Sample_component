#!/usr/bin/env python
import os

from pkg_resources import parse_requirements
from setuptools import setup, find_packages


_PATH_ROOT = os.path.dirname(__file__)


def _load_requirements(path_dir: str = _PATH_ROOT, file_name: str = "requirements.txt") -> list:
    reqs = parse_requirements(open(os.path.join(path_dir, file_name)).readlines())
    return list(map(str, reqs))


setup(
    name='lit_slack',
    version='0.0.0',
    description='Describe Your Cool Component',
    author='',
    author_email='',
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url='https://github.com/PyTorchLightning/lightning-component-template',
    install_requires=_load_requirements(),
    packages=find_packages(exclude="tests"),
)
