import sys
import os
import numpy as np
  
from astropy.io import fits
from astropy import units as u

import ccdproc 
from ccdproc import CCDData

import argparse
import pylab as pl


parser = argparse.ArgumentParser(description='Create a 1-D difference spectra')
parser.add_argument('afile', help='Reference file for spectra')
parser.add_argument('bfile', help='File to be compared')
parser.add_argument('--yc', help='Central row of object', type=int)
parser.add_argument('--dy', help='Half width of object', type=int)
args = parser.parse_args()

accd = CCDData.read(args.afile)
bccd = CCDData.read(args.bfile)

y1 = args.yc - args.dy
y2 = args.yc + args.dy
aspec = accd.data[y1:y2,:].sum(axis=0)
bspec = bccd.data[y1:y2,:].sum(axis=0)

xarr = np.arange(len(aspec))
warr = 1.0 * xarr

pl.figure()
pl.subplot(311)
pl.plot(warr, aspec)
pl.plot(warr, bspec)
pl.ylabel('Counts', size='x-large')
pl.subplot(312)
pl.plot(warr, bspec-aspec)
pl.ylabel('Diff', size='x-large')
pl.subplot(313)
pl.plot(warr, bspec/aspec)
pl.ylabel('Ratio', size='x-large')
pl.xlabel('Wavelength', size='x-large')
pl.show()

