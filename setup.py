# Automatically created by: scrapy deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.1',
    packages     = find_packages(),
    scripts      = ['bin/hello2.py'],
    entry_points = {'scrapy': ['settings = kickbot.settings']},
)
