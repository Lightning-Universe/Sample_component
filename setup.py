#!/usr/bin/env python
import os

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

_PATH_ROOT = os.path.dirname(__file__)


def _load_requirements(path_dir: str = _PATH_ROOT, file_name: str = "requirements.txt") -> list:
    reqs = parse_requirements(open(os.path.join(path_dir, file_name)).readlines())
    return list(map(str, reqs))


setup(
    name="lit-slack",
    version="0.1.0",
    description="Describe Your Cool Component",
    author="Lightning-AI",
    author_email="name@lightning.ai",
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url="https://github.com/Lightning-Universe/Sample_component",
    long_description="""Some long description or load readme""",
    install_requires=_load_requirements(),
    packages=find_packages(exclude=["tests", "tests.*"]),
)
