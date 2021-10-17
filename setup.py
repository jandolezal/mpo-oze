from setuptools import setup

setup(
    name='mpo',
    version='0.0.1',
    py_modules=[
        'mpo',
        'links',
        'parse',
        ],
    install_requires=[
        'beautifulsoup4',
        'camelot-py',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'mpo = mpo:main',
        ]
    }
)