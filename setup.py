from setuptools import setup, find_packages

setup(
    name='chemical_engineering_tools',
    version='0.1',
    packages=find_packages(),
    description='Chemical engineering calculation tools for mass balance, energy balance, and stoichiometry',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Boss Erika',
    url='https://github.com/Yuwi234/chemical_engineering_tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
    python_requires='>=3.6',
)
