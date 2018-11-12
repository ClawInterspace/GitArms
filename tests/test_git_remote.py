# -*- encoding: utf-8 -*-
import unittest
from unittest import mock
import subprocess

from ddt import ddt, data, unpack

from utils.git_remote import get_remote


@ddt
class TestGitRemote(unittest.TestCase):

    def setUp(self):
        pass

    @unpack
    @data(
        [b'origin\tgit@github.com:ClawInterspace/GitArms.git (fetch)\n'
        b'origin\tgit@github.com:ClawInterspace/GitArms.git (push)\n',
        "git@github.com:ClawInterspace/GitArms.git"],
        [b'origin\tgit@gitlab.com:ClawSpace/Practice/mypylab.git (fetch)\n'
        b'origin\tgit@gitlab.com:ClawSpace/Practice/mypylab.git (push)\n',
        "git@gitlab.com:ClawSpace/Practice/mypylab.git"]
    )
    def test_get_remote(self, mock_output, expected_url):
        
        subprocess.check_output = \
            mock.Mock(return_value=(mock_output, "error"))
        self.assertEqual(expected_url, get_remote(''))

    def test_update_remote(self):
        pass


if __name__ == '__main__':
    unittest.main()