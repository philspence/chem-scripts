import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='chem-scripts',
    version='0.1',
    author='Phil Spence',
    author_email='philspence91@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/philspence/chem-scripts',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)

