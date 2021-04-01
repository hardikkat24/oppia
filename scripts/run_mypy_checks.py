import argparse
import os
import subprocess

# import python_utils

# list of strictly typed files
strict_typed_files = ['core/controllers/admin.py', 'core/controllers/base.py', 'core/controllers/admin_test.py']

NOT_STRICT_CONFIG_FILE_PATH = os.path.join('.','mypy.ini')
STRICT_CONFIG_FILE_PATH = os.path.join('.','mypy-strict.ini')

_PARSER = argparse.ArgumentParser(
    description="""
Type checking script for Oppia codebase.
""")

_PARSER.add_argument(
    '--strict',
    help='If true, checks typing in strict mode',
    action='store_true')

_PARSER.add_argument(
    '--files',
    help='Files to type-check',
    action='extend',
    nargs='+'
    )

def main(args=None):
    unused_parsed_args = _PARSER.parse_args(args=args)
    # python_utils.PRINT('Type checking the oppia codebase')

    if unused_parsed_args.strict:
        path = STRICT_CONFIG_FILE_PATH
    else:
        path = NOT_STRICT_CONFIG_FILE_PATH

    if unused_parsed_args.files:
        process = subprocess.Popen(
            ['mypy', '--config-file', path, ] + unused_parsed_args.files,
            stdin=subprocess.PIPE)

    # take files from config-file
    else:
        process = subprocess.Popen(
            ['mypy', '--config-file', path] + strict_typed_files ,
            stdin=subprocess.PIPE)


if __name__ == '__main__': # pragma: no cover
    main()
