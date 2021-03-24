import argparse
import os
import subprocess

# import python_utils

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

files = ['core/domain/*', 'core/controllers/']

def main(args=None):
    unused_parsed_args = _PARSER.parse_args(args=args)
    # python_utils.PRINT('Type checking the oppia codebase')

    if unused_parsed_args.strict:
        path = STRICT_CONFIG_FILE_PATH
    else:
        path = NOT_STRICT_CONFIG_FILE_PATH

    subprocess.call(
        ['mypy', '--config-file', path],
        stdin=subprocess.PIPE)


if __name__ == '__main__': # pragma: no cover
    main()
