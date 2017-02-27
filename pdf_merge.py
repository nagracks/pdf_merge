#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "12-07-2016"
__license__   = "MIT"
__copyright__ = "Copyright © 2016 nagracks"

import argparse

import PyPDF2


def merge_it(files, output_name='merged_file.pdf'):
    """Merge PDF files

    :files: list of pdf files
    :output_name: name of output merged file
    :returns: None
    """
    if len(files) <= 1:
        return
    merger = PyPDF2.PdfFileMerger()
    for filename in files:
        merger.append(open(filename, 'rb'))
    merger.write(output_name)


if __name__ == "__main__":
    # Parse commandline options with argparse
    parser = argparse.ArgumentParser(description="PDF Merge script")
    parser.add_argument(
            'files', 
            action='store', 
            nargs='*',
            help="pdf files"
            )
    parser.add_argument(
            '-o', '--output-file',
            dest='output_file',
            action='store',
            help="output file name. defaults to `merged_file.pdf`"
            )
    args = parser.parse_args()

    if args.output_file:
        merge_it(args.files, args.output_file)
    else:
        merge_it(args.files)
