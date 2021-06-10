# coding: utf-8
#
# Copyright 2020 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for MyPy tyoe check runner script."""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

import subprocess
import tempfile

from core.tests import test_utils
from scripts import run_mypy_checks

PYTHON_CMD = 'python3'
MYPY_SCRIPT_MODULE = 'scripts.run_mypy_checks'


class MypyScriptChecks(test_utils.GenericTestBase):
    """Tests for MyPy type check runner script."""

    def setUp(self):
        super(MypyScriptChecks, self).setUp()
        process_success = subprocess.Popen(['echo', 'test'], stdout=subprocess.PIPE)
        def mock_popen_success(unused_cmd, stdout):  # pylint: disable=unused-argument
            return process_success

        process_failure = subprocess.Popen(['test'], stdout=subprocess.PIPE)
        def mock_popen_failure(unused_cmd, stdout):  # pylint: disable=unused-argument
            return process_failure

        self.popen_swap_success = self.swap(subprocess, 'Popen', mock_popen_success)
        self.popen_swap_failure = self.swap(subprocess, 'Popen', mock_popen_failure)

    def test_get_cmd_without_files(self):
        cmd = run_mypy_checks._get_cmd(None)
        self.assertIn('--exclude', cmd)
        self.assertIn('--config-file', cmd)

    def test_get_cmd_with_files(self):
        cmd = run_mypy_checks._get_cmd([['file1.py', 'file2.py']])
        self.assertIn('file1.py', cmd)
        self.assertIn('file2.py', cmd)
        self.assertNotIn('--exclude', cmd)
        self.assertIn('--config-file', cmd)

    def test_running_script_with_success(self):
        with self.popen_swap_success:
            process = subprocess.Popen([PYTHON_CMD, '-m', MYPY_SCRIPT_MODULE], stdout=subprocess.PIPE)
            output = process.communicate()
            self.assertEqual(output[0], 'test\n')

    def test_running_script_with_failure(self):
        with self.popen_swap_failure:
            process = subprocess.Popen([PYTHON_CMD, '-m', MYPY_SCRIPT_MODULE], stdout=subprocess.PIPE)
            output = process.communicate()
            self.assertEqual(output[0], '')
