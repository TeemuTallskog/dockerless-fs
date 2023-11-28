from setuptools import setup, find_packages

setup(
    name='dockerless-fs',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dockerless-fs=dockerless_fs.__main__:main',
        ],
    },
    author='Teemu Tallskog',
    description='Explore Docker image filesystem without Docker!',
    license="BSD 3-Clause",
    url="https://github.com/TeemuTallskog/dockerless-fs"
)