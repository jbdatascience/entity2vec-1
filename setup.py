try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='entity2vec',
    version='1.0',
    packages=['entity2vec', ],
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    install_requires=[
     'gensim',
     'networkx',
     'pandas',
     'SPARQLWrapper'
    ]
)
