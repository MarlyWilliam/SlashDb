from setuptools import setup, find_packages

setup(
    name='task',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyramid',
        'sqlalchemy',
        'mako',
    ],
    extras_require={
        'testing': ['pytest'],
    },
    entry_points={
        'paste.app_factory': [
            'main = task:main',
        ],
    },
)