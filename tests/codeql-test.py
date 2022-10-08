import argparse
import os


def open_path(file_path):
    file = open(file_path, 'r')


if '__name__' == '__main__':
    parser = argparse.ArgumentParser (
        conflict_handler = 'resolve',
        fromfile_prefix_chars = '@'
        )


    parser.add_argument ('-file', '--file', dest = 'file',
                         help = 'JSON configuration file for multiple payloads and embedded drivers.')

    args = parser.parse_args()
    open_path (args.file)
