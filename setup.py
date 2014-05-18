# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = """
django-pipeline compiler for node-sass.
"""

setup(
    name='django-pipeline-node-sass',
    version='0.0.1',
    description=description,
    long_description=description,
    author='jrpotter',
    author_email='jrpotter@gmail.com',
    url='https://github.com/jrpotter/django-pipeline-node-sass',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities',
    ]
)
