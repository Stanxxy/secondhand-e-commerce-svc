"""Python setup.py for secondhand_e_commerce_svc package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("secondhand_e_commerce_svc", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="secondhand_e_commerce_svc",
    version=read("secondhand_e_commerce_svc", "VERSION"),
    description="Awesome secondhand_e_commerce_svc created by Stanxxy",
    url="https://github.com/Stanxxy/secondhand-e-commerce-svc/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Stanxxy",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["secondhand_e_commerce_svc = secondhand_e_commerce_svc.__main__:main"]
    },
    extras_require={
        "test": read_requirements("requirements-test.txt")
        + read_requirements("requirements-base.txt")
    },
)
