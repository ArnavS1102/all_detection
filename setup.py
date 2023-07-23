from setuptools import find_packages,setup

setup(name="alldetection",
    version="1.0",
    install_requires=[],
    packages=find_packages(exclude="notebooks")
)