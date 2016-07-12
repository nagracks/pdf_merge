#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "12-07-2016"
__license__   = "GPL3"
__copyright__ = "Copyright © 2016 nagracks"

import argparse

# external modules #
import PyPDF2

def parse_args():
    """Parse commandline args with argparse
    :returns: args

    """
    parser = argparse.ArgumentParser(description="PDF Merge script")
    # Positional args #
    parser.add_argument('files',
                        action='store',
                        nargs='*',
                        help="pdf files")

    # Optional args #
    parser.add_argument('-o',
                        '--output-file',
                        dest='output_file',
                        action='store',
                        help="output file name. defaults to `merged_file.pdf`")

    args = parser.parse_args()
    return args

class PDFMerge(object):

    """PDF Merge"""

    def __init__(self, files):
        """Initialise class
        :files: input files
        """
        self.files = files

    def merge_it(self, output_name='merged_file.pdf'):
        """Merge PDF files
        :returns: None
        """
        # Initialise merger class #
        merger = PyPDF2.PdfFileMerger()

        # Iterate through input pdf files #
        # Append pdfs one after another #
        for filename in self.files:
            merger.append(open(filename, 'rb'))

        # Finally write to file #
        merger.write(output_name)

def main():
    """Main function
    :returns: TODO
    """
    # Commandline args #
    args = parse_args()

    # Initialise class #
    merge = PDFMerge(args.files)

    # Conditions when merging PDFs #
    # if output filename is given, use it as output filename #
    if args.output_file:
        merge.merge_it(args.output_file)
    # Else merge it with default name `merged_file.pdf` #
    else:
        merge.merge_it()

if __name__ == "__main__":
    main()
