from setuptools import setup
import pkgutil

setup(
    name='crawler-similarweb',
    version='',
    packages=['similarweb', 'similarweb.spiders'],
    package_data={
        'crawler-similarweb': ['domains.json']
    },
    entry_points={
        'scrapy': ['settings = crawler-similarweb.settings']
    },
    zip_safe=False,
    url='',
    license='',
    author='ligo',
    author_email='',
    description=''
)

data = pkgutil.get_data("crawler-similarweb", "domains.json")