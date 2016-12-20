# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='guess',
    version='0.0.1',
    description='A simple web-based number guess game',
    author='Jianing Yang',
    author_email='jianingy.yang@gmail.com',
    url='',
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'guess=guess.server:main',
        ]
    },
    packages=['guess'],
    classifiers=[
    ],
)
