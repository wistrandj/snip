import os
import click
import logging

log = logging.getLogger(__name__)

SNIP_ROOT_FILE = os.path.join(os.path.dirname(__file__), 'install.dir')

def snip_root():
    with open(SNIP_ROOT_FILE, 'r') as fd:
        return fd.read()

def snip_pack_dir():
    return os.path.join(snip_root(), 'pack')

def where():
    print(snip_pack_dir())

def main():
    print('here', SNIP_ROOT)

# Note(wistrandj): Click option is not required by default but argument
# is required unless otherwise stated.

@click.command()
@click.option('--file')
@click.argument('files', required=False)
def snip_file(file, files):
    file = file or files
    if not file:
        log.error('Missing file argument')

    for dir, subdirs, files in os.walk(snip_pack_dir()):
        for it in files:
            if it == file:
                filepath = os.path.join(dir, it)
                with open(filepath, 'r') as fd:
                    content = fd.read()
                    print(content)
                    return

