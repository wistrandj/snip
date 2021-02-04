from setuptools import setup
import os

# Note(wistrandj): Change this to the target location where snippets
# will be saved and edited. Or install a config file in user HOME
# directory.
SNIP_ROOT = '/usr/local/src/external/snip'
# SNIP_ROOT = os.getcwd()
SNIP_ROOT_FILE = './app/install.dir'

def install_snip_install_dir_file():
    requirements_txt = os.path.join(SNIP_ROOT, 'app', 'requirements.txt')
    if not os.path.isfile(requirements_txt):
        raise RuntimeError(f'Not in snip root dir')
    if not os.path.isdir(os.path.dirname(SNIP_ROOT_FILE)):
        raise RuntimeError(f'Missing source folder {SNIP_ROOT_FILE}')

    fullpath = os.path.abspath(SNIP_ROOT_FILE)
    with open(SNIP_ROOT_FILE, 'w') as fd:
        fd.write(SNIP_ROOT)

install_snip_install_dir_file()

setup(
    name='snip',
    author='Jasse Wistrand <jasse.wistrand@iki.fi>',
    packages=['app'],
    entry_points={
        'console_scripts': [
            'snip=app.main:main',
            'snip-where=app.main:where',
            'snip-file=app.main:snip_file',
            'snip-project=app.main:snip_project',
        ]
    },
    include_package_data=True,
)

