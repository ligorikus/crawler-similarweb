from setuptools import setup, find_packages

setup(
    name='ligosimilar',
    version='1.0',
    packages=find_packages(),
    package_data={
        'ligosimilar': ['domains.json']
    },
    entry_points={
        'scrapy': ['settings = ligosimilar.settings']
    },
    zip_safe=False,
    author='ligo',
)
