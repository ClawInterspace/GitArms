# -*- encoding: utf-8 -*-
import os
import io

import subprocess

def _is_git_repo(path):
    repo = os.path.join(os.path.abspath(path), '.git')
    return os.path.isdir(repo)


def get_remote(repo_path):
    """
    """
    try:
        output = subprocess.check_output(['git', '-C', repo_path, 'remote', '-v'])
    except:
        raise Exception('Get remote %s error' % repo_path)

    lines = io.StringIO(output.decode('utf-8')).readlines()
    remote_url = lines[0].split()[1]

    return remote_url

def update_remote(repo_path, protocol, host, port, path):
    pass

if __name__ == '__main__':
    pass