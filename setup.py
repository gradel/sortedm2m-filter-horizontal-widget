#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import sys
from setuptools import setup


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts),
                       encoding='utf8').read()


try:
    bytes
except NameError:
    bytes = str


class UltraMagicString(object):
    '''
    Taken from
    http://stackoverflow.com/questions/1162338/whats-the-right-way-to-use-unicode-metadata-in-setup-py
    '''
    def __init__(self, value):
        if not isinstance(value, bytes):
            value = value.encode('utf8')
        self.value = value

    def __bytes__(self):
        return self.value

    def __unicode__(self):
        return self.value.decode('UTF-8')

    if sys.version_info[0] < 3:
        __str__ = __bytes__
    else:
        __str__ = __unicode__

    def __add__(self, other):
        return UltraMagicString(self.value + bytes(other))

    def split(self, *args, **kw):
        return str(self).split(*args, **kw)


long_description = UltraMagicString('\n\n'.join((
    read('README.rst'),
    read('CHANGES.rst'),
)))


setup(
    name = 'django-sortedm2m-filter-horizontal-widget',
    version = find_version('sortedm2m_filter_horizontal_widget', '__init__.py'),
    url = 'http://github.com/svleeuwen/django-sortedm2m-filter-horizontal-widget',
    license = 'BSD',
    description =
        'Horizontal filter widget for django-sortedm2m',
    long_description = long_description,
    author = UltraMagicString('Sander van Leeuwen'),
    author_email = 'replytosander@gmail.com',
    packages = ['sortedm2m_filter_horizontal_widget'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    install_requires = ['django-sortedm2m'],
)
