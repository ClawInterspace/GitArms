# -*- encoding: utf-8 -*-
import os

from utils.git_remote import get_remote


def get_all_git_repos(root_path: str):

    for dirpath, dirs, files in os.walk(root_path):
        pass


def update_git_repo_by(search_url, target_url):
    pass


"""
given a root folder,
if the remote url is http://tfs.cybersoft4u.com:8080/xxxx,
    update to ssh://192.168.91.131/xxxx
"""
