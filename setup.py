# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="vanagand-package-study", # the name that you will install via pip
    version="0.0.1",
    author="Michel Laporte",
    author_email="michlaporte15@gmail.com",
    description="A package study that does a few things",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Vanagand/vanagand-lambdata-13",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)