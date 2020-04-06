import os
from setuptools import setup

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(CUR_DIR, "README.md")
with open("README.md", "r") as fd:
    long_description = fd.read()

setup(
    name = 'xlsxtpl',
    version = "0.2",
    author = 'Zhang Yu',
    author_email = 'zhangyu836@gmail.com',
    url = 'https://github.com/zhangyu836/python-xlsx-template',
    packages = ['xlsxtpl'],
	install_requires = ['openpyxl', 'jinja2', 'six'],
    description = ( 'A python module to generate xlsx files from a xlsx template' ),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    platforms = ["Any platform "],
    license = 'MIT',
    keywords = ['xlsx', 'spreadsheet', 'workbook', 'template']
)