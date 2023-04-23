from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Sorting files in directory',
    author='Anastasia Shevchenko',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)