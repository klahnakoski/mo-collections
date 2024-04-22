# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","Programming Language :: Python :: 3.11","Programming Language :: Python :: 3.12"],
    description='More Collections! Some useful data structures for dealing with Data',
    extras_require={"tests":["mo-testing>=7.562.24075"]},
    include_package_data=True,
    install_requires=["mo-dots==9.596.24113","mo-future==7.584.24095","mo-kwargs==7.596.24113","mo-logs==8.597.24113"],
    license='MPL 2.0',
    long_description="# More Collections\n\nSome useful data structures for collections of data\n\n\n### Class `Index`\n\nProvide indexing for a list. Inner properties can be used for keys, and keys can be tuples of properties.  \n\n### Class `UniqueIndex`\n\nSame as Index, but includes checks and optimization to ensure members' keys are unique.\n\n### Class `Queue`\n\nA `Queue` is a list, with `add()` and `pop()`. It ensures members in the queue are not duplicated by not adding the ones already found in the queue.\n\n### Class `Matrix`\n\nA multidimensional grid of values that can be used like a `Mapping` from a-tuple-of-coordinates to the value at that coordinate. Plus a few other convenience methods.\n\nThis is a naive implementation. The hope it is a simple facade to a faster implementation.\n\n### Class `Relation`\n\nStore the many-to-many relations between two domains     ",
    long_description_content_type='text/markdown',
    name='mo-collections',
    packages=["mo_collections"],
    url='https://github.com/klahnakoski/mo-collections',
    version='5.597.24113'
)