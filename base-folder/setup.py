from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A basic hello package'

# Setting up
setup(
    name="CalculatorPro",
    version=VERSION,
    author="codechamp2006 (Sagnik Ray)",
    author_email="sagnikraycoder27@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    scripts=[],
    keywords=['python', 'calculator', 'mentalMaths'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
