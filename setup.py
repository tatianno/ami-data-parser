import os
from setuptools import setup, find_packages


with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='ami-data-parser',
    version='0.0.1',
    license='MIT License',
    author='Tatianno Alves',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='tferreiraalves@gmail.com',
    keywords='asterisk manager interface ami parser data',
    description=u'AMI parser data',
    packages=find_packages(include=['ami_data_parser', 'ami_data_parser.*']),
)