import os
import shutil
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

@click.command()
@click.option('--dir', default='.')
@click.argument('project', required=True)
def snip_project(dir: str, project: str):
    here_dirpath = os.path.abspath(dir)
    if os.path.isdir(here_dirpath):
        is_empty = len(os.listdir(here_dirpath)) == 0
        if not is_empty:
            log.error('The folder is not empty')
            return
    else:
        os.mkdir(here_dirpath)

    pack_dir = os.path.abspath(snip_pack_dir())
    template_dir = None
    template_fullpath = None

    for dir, subdirs, files in os.walk(pack_dir):
        for it in subdirs:
            if it == project:
                template_fullpath = os.path.join(dir, it)
                break
    if not template_fullpath:
        log.error(f'No project {project} found')
        return

    files_short = []

    for dir, subdirs, files in os.walk(template_fullpath):
        for it in files:
            it_fullpath = os.path.join(dir, it)
            prefix = pack_dir + '/' + project + '/'
            it_short = it_fullpath.replace(prefix, '')
            files_short.append(it_short)

    sources = [os.path.join(template_fullpath, file) for file in files_short]
    targets = [os.path.join(here_dirpath, file) for file in files_short]
    cmds = dict(zip(sources, targets))

    # Todo(wistrandj): Copy permission bits
    for source, target in zip(sources, targets):
        target_dir = os.path.dirname(target)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)
        shutil.copy(source, target)

