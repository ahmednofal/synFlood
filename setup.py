#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

tool_name="syner"
version_num = "0.0.1"
author_name = "Dylan Hudson"
email = "dhudson@azcwr.org"
setuptools.setup(name=tool_name,
        version=version_num,
        author=author_name,
        author_email=email,
        description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/XXXTheInternXXX/synFlood",
        packages=setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
        ],
        scripts = [
                'core/syner'
        ],
        install_requires=[
            "scapy==2.4.0"
            ]
)
