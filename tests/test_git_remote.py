# -*- encoding: utf-8 -*-
import unittest
from unittest import mock
import subprocess

from ddt import ddt, data, unpack

from gitarms.utils.git_remote import get_remote, update_remote


@ddt
class TestGitRemote(unittest.TestCase):

    @unpack
    @data(
        [b'origin\tgit@github.com:ClawInterspace/GitArms.git (fetch)\n'
         b'origin\tgit@github.com:ClawInterspace/GitArms.git (push)\n',
         "git@github.com:ClawInterspace/GitArms.git"],
        [b'origin\tgit@gitlab.com:ClawSpace/Practice/mypylab.git (fetch)\n'
         b'origin\tgit@gitlab.com:ClawSpace/Practice/mypylab.git (push)\n',
         "git@gitlab.com:ClawSpace/Practice/mypylab.git"]
    )
    def test_get_remote(self, mock_output: str, expected_url: str):
        """
        @note: ensure that the parsing method is correct
        """
        subprocess.check_output = \
            mock.Mock(return_value=(mock_output, "error"))
        self.assertEqual(expected_url, get_remote(''))

    @unpack
    @data(
        [r'git -C "/home/alan/workspace/open-source/flask-project" '
         r'remote set-url "git@gitlab.com:ClawSpace/Practice/mypylab.git"',
         r'/home/alan/workspace/open-source/flask-project',
         "git@gitlab.com:ClawSpace/Practice/mypylab.git"]
    )
    def test_update_remote(
        self,
        expected_command: str,
        repo_path: str,
        new_repo_url: str,
        remote: str = 'origin'
    ):
        """
        @Note: ensure that call the correct command
        """
        with mock.patch('subprocess.call') as mock_subprocess_call:
            update_remote(repo_path, new_repo_url, remote)
            mock_subprocess_call.assert_called_with(
                expected_command,
                shell=True
            )


if __name__ == '__main__':
    unittest.main()
