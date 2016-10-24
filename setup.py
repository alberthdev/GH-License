from setuptools import setup, find_packages

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

setup(
    name="gh-license",
    version="0.1a",
    author="Mte90",
    install_requires=open(os.path.join(BASE_DIR, "requirements.txt")).readlines(),
    license="GPLv3",
    description="Scan github repositories for missing license files and add them",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gh-license=ghlicense.cmd:main'
        ]
    }
)
