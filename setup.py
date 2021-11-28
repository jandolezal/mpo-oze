from setuptools import find_packages, setup


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='mpo-oze',
    version='0.0.2',
    description='Parse reports covering renewables published by the Czech Ministry of Trade and Industry',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jandolezal/mpo-oze',
    author='Jan Doležal',
    author_email='aswlk2zn2@mozmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=['mpo'],
    install_requires=[
        'beautifulsoup4',
        'camelot-py[base]',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'mpo=mpo.__main__:main',
        ]
    }
)
