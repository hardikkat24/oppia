import argparse
import os
import subprocess

# import python_utils

# list of non-strictly typed files and directories
not_strict_typed_files_and_directories = [
    'core/',
    'scripts',
    'third_party',
    'extensions/',
    'jobs/',
    'core/controllers/admin.py',
]

# list of typed files
strict_typed_files = [
    'core/controllers/admin.py',
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
            ['mypy', '--namespace-packages', '--explicit-package-bases', '--config-file', CONFIG_FILE_PATH] + unused_parsed_args.files,
            stdin=subprocess.PIPE)

    # take files from config-file
    else:
        cmd = ['mypy', '--namespace-packages', '--explicit-package-bases', '--exclude', '|'.join(not_strict_typed_files_and_directories),
        '--config-file', CONFIG_FILE_PATH, '.'] + strict_typed_files

        process = subprocess.Popen(cmd, stdin=subprocess.PIPE)


if __name__ == '__main__': # pragma: no cover
    main()
