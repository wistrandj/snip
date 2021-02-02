from setuptools import setup

setup(
    name='foobar',
    author='Jasse Wistrand <jasse.wistrand@iki.fi>',
    packages=['app'],
    entry_points={
        'console_scripts': [
            'app=app.main:main',
        ]
    },
    scripts = ['bin/foo.sh'],
    include_package_data=True,
)

