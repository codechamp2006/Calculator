from setuptools import setup, find_packages
import codecs
import os

# long description
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

VERSION = '2.3'
DESCRIPTION = 'Fully integrated and packaged all sorts of mathematical equations and common problems, series.'


# Setting up
setup(
    name="CalculatorPro",
    version=VERSION,
    author="codechamp2006 (Sagnik Ray)",
    author_email="sagnikraycoder27@gmail.com",
    description=DESCRIPTION,
    long_description= LONG_DESCRIPTION,
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
