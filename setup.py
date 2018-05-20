from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    scripts      = ['cleaner_to_CSV.py'],
    entry_points = {'scrapy': ['settings = A308366.settings']},
)
