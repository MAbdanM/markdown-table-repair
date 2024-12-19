from setuptools import setup, find_packages

setup(
    name='markdown-table-repair',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    description='A package to repair and clean malformed markdown tables.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Muhammad Abdan Mulia',
    author_email='abdanmulia@gmail.com',
    url='https://github.com/MAbdanM/markdown-table-repair',
)