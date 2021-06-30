#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Sentry-c3-WxWork",
    version='1.0.0',
    author='c3jbz',
    author_email='18608411988@163.com',
    url='https://github.com/c3jbz/sentry-c3-wxwork',
    description='A Sentry extension which send errors stats to wxwork',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry wxwork',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=21.6.1',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_c3_wxwork = sentry_c3_wxwork.plugin:WxWorkPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
