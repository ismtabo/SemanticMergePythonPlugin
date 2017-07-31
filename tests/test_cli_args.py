import os
import unittest


class TestCLIArgs(unittest.TestCase):

    def setUp(self):
        self.python_command_format = "python smpy_plugin {args}"

    def test_no_args(self):
        self.assertNotEqual(os.system(self.python_command_format.format(args="")), 0)

    def test_too_few_args(self):
        self.assertNotEqual(os.system(self.python_command_format.format(args="shell")), 0)

    def test_unsupported_mode(self):
        self.assertNotEqual(os.system(self.python_command_format.format(args="unsupported flag.txt")), 0)
