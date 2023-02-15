#!/usr/bin/env python
import os
from importlib.util import module_from_spec, spec_from_file_location

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

_PATH_ROOT = os.path.dirname(__file__)


def _load_py_module(fname: str, pkg: str = "lit_slack"):
    spec = spec_from_file_location(os.path.join(pkg, fname), os.path.join(_PATH_ROOT, pkg, fname))
    py = module_from_spec(spec)
    spec.loader.exec_module(py)
    return py


def _load_requirements(path_dir: str = _PATH_ROOT, file_name: str = "requirements.txt") -> list:
    reqs = parse_requirements(open(os.path.join(path_dir, file_name)).readlines())
    return list(map(str, reqs))


about = _load_py_module("__about__.py")
with open(os.path.join(_PATH_ROOT, "README.md"), encoding="utf-8") as fo:
    readme = fo.read()


setup(
    name="lit-slack",
    version=about.__version__,
    description=about.__docs__,
    author=about.__author__,
    author_email=about.__author_email__,
    license=about.__license__,
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url=about.__homepage__,
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=_load_requirements(),
    packages=find_packages(exclude=["tests", "tests.*"]),
)
