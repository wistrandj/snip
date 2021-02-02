# Snip

Save snippets, templates and any code or text in a git repository.

### Usage

Print a template script.

    $ mkdir new-project
    $ cd new-project
    $ snip-file setup.py | tee ./setup.py
    from setuptools import setup
    setup(
      name='foobar',
      packages=['app'],
    )

### Install

Fetch the code to a well known location e.g. `/usr/local/external/snip`

    $ cd /usr/local/external
    $ git clone git@github.com:wistrandj/snip.git
    $ cd snip

Change the install directory in setup script.

    $ vim ./app/setup.py
    SNIP_ROOT = '/usr/local/src/external/snip'

Install the project

    $ pip install -r requirements.txt

