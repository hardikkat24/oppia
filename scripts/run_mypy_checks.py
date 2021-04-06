import argparse
import os
import subprocess

# import python_utils

# list of non-strictly typed files
not_strict_typed_files = [
    'core/controllers/base.py',
    'core/controllers/admin.py',
    'core/controllers/base_test.py',
    'core/controllers/admin_test.py',
    'scripts',
    'third_party'
]

CONFIG_FILE_PATH = os.path.join('.','mypy-strict.ini')

_PARSER = argparse.ArgumentParser(
    description="""
Type checking script for Oppia codebase.
""")

_PARSER.add_argument(
    '--files',
    help='Files to type-check',
    action='extend',
    nargs='+'
    )

def main(args=None):
    unused_parsed_args = _PARSER.parse_args(args=args)
    # python_utils.PRINT('Type checking the oppia codebase')


    if unused_parsed_args.files:
        process = subprocess.Popen(
            ['mypy', '--config-file', CONFIG_FILE_PATH] + unused_parsed_args.files,
            stdin=subprocess.PIPE)

    # take files from config-file
    else:
        cmd = ['mypy', '--exclude', '|'.join(not_strict_typed_files),
        '--config-file', CONFIG_FILE_PATH, '.']

        process = subprocess.Popen(cmd, stdin=subprocess.PIPE)


if __name__ == '__main__': # pragma: no cover
    main()
