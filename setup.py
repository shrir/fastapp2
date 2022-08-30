import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Fastapp2',
    version='0.1',
    description=('Fastapp2 app'),
    license='MIT',
    keywords='',
    packages=['app'],
    long_description=read('README.md'),
    python_requires='>=3.9, <4',
    install_requires=[
        'fastapi',
        'uvicorn',
        'pydantic',
    ],
    test_requires=['pytest', 'coverage', 'requests', 'greenlet'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Application',
        'License :: OSI Approved :: MIT License'
    ]
)
