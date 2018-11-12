# -*- encoding: utf-8 -*-
import logging
import os
import io
import subprocess


def _is_git_repo(path: str):
    repo = os.path.join(os.path.abspath(path), '.git')
    return os.path.isdir(repo)


def get_remote(repo_path: str):
    """
    @return: remote url of the git repository
    """
    cmd = 'git -C %s remote -v' % repo_path
    try:
        result = subprocess.check_output(cmd, shell=True)
    except:
        raise Exception('Get remote %s error' % repo_path)

    output = result[0]
    lines = io.StringIO(output.decode('utf-8')).readlines()
    remote_url = lines[0].split()[1]

    return remote_url


def update_remote(repo_path: str, new_repo_url: str, remote: str = 'origin'):
    """
    """
    cmd = 'git -C "%s" remote set-url "%s"' % (repo_path, new_repo_url)
    try:
        subprocess.call(cmd, shell=True)
    except Exception:
        logging.error('Update "%s" fail under "%s"' %
                      (new_repo_url, repo_path))
        raise


if __name__ == '__main__':
    pass
