import os
from setuptools import setup

readme = open('README.md').read()

requirements = ['click', 'feedparser', 'BeautifulSoup']

setup(
    name = "whatsnew",
    version = "0.12",
    author = "Patrick Tyler Haas",
    author_email = "patrick.tyler.haas@gmail.com",
    description = ("A lightweight, convenient tool to get an overview of the day's headlines right from your command line."),
    license = "MIT",
    keywords = "",
    url = "https://github.com/haaspt/whatsnew",
    scripts=['main.py', 'newsfeeds.py', 'config.py'],
    install_requires=requirements,
    long_description=readme,
    entry_points = {
        'console_scripts': [
            'whatsnew = main:main'
            ],
        },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        ],
    )
