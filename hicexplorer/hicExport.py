#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import division
from os.path import splitext
import sys
import argparse
from hicexplorer import HiCMatrix as hm
from hicexplorer._version import __version__
from scipy import sparse



def parsearguments(args=None):
    """
    get command line arguments
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Saves a matrix in .npz format using a plain text format.')

    # define the arguments
    parser.add_argument('--matrix', '-m',
                        help='matrix to use',
                        metavar='.npz fileformat',
                        required=True)

    parser.add_argument('--outFileName', '-o',
                        help='File name to save the plain text matrix',
                        type=argparse.FileType('w'),
                        required=True)

    parser.add_argument('--chromosomeOrder',
                        help='Chromosomes and order in which the '
                             'chromosomes should be plotted. This option '
                             'overrides --region and --region2 ',
                        nargs='+')

    parser.add_argument('--outputFormat',
                    help='Output format. There are two possibilities: "dekker" and "ren". '
                         'The dekker format outputs the whole matrix where the '
                         'first column and first row are the bin widths and labels. '
                         'The "ren" format is a list of tuples of the form '
                         'chrom, bin_star, bin_end, values.',
                    default='dekker',
                    choices=['dekker', 'ren'])

    parser.add_argument('--clearMaskedBins',
                        help='if set, masked bins are removed from the matrix. Masked bins '
                             'are those that do not have any values, mainly because they are'
                             'repetitive regions of the genome',
                        action='store_true')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(__version__))


    return parser.parse_args(args)


if __name__ == "__main__":
    ARGS = parsearguments()

    hic_ma = hm.hiCMatrix(ARGS.matrix)
    if ARGS.chromosomeOrder:
        hic_ma.keepOnlyTheseChr(ARGS.chromosomeOrder)

    if ARGS.clearMaskedBins:
        hic_ma.maskBins(hic_ma.nan_bins)

    sys.stderr.write('saving...\n')
    matrix_name = ARGS.outFileName.name
    ARGS.outFileName.close()
    if ARGS.outputFormat == 'dekker':
        hic_ma.save_dekker(matrix_name)
    else:
        hic_ma.save_bing_ren(matrix_name)
