from setuptools import setup, find_packages

setup(
    name='transactify',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Venkatraman.R',
    author_email='ramsunvtech@gmail.com',
    description='A Python module for predicting transaction categorization',
    # Add contributors
    author='jaswanth gutti',
    author_email='jeswanth.gutti@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/web-slate/transactify',
    license='MIT',
)