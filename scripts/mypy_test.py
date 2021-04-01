from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

import os
import subprocess

from core.tests import test_utils

# import python_utils
PYTHON_CMD = 'python3'
SCRIPT = 'scripts.run_mypy_checks'

class MypyTests(test_utils.GenericTestBase):

    def setUp(self):
        super(MypyTests, self).setUp()

    def _process_for_file(self, filename):
        process = subprocess.Popen(
            [PYTHON_CMD, '-m', SCRIPT, '--files', 'mypy-tests/' + filename],
            stdout=subprocess.PIPE)
        return process

    def test_1(self):
        process = _process_for_file('file1.py')
        print(process)

