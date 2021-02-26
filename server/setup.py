from setuptools import setup, find_packages
from os import path

setup(
    name='aiohttp-pytest-example',
    version='0.0.1',
    description='aiohttp pytest example',
    url='https://github.com/mrUmberto/aiohttp-pytest-example',
    author='Alexander Odegov',
    author_email='alexander.odegov@protonmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7.4'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'aiohttp==3.7.4',
        'aiohttp_cors==0.7.0',
        'aiopg==1.0.0',
        'alembic==1.4.2',
        'peewee==3.13.1',
        'peewee-async==0.7.0',
        'pydantic==1.5.1'
    ]
)
