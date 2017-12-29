import numpy as np
from waveletsmooth import smooth
import astropy.io.fits as pyfits
import os, sys, glob, time
from decimal import Decimal

secperday = 3600 * 24
cutoff = 0.2

now = time.time()

filename = sys.argv[1] 
if len(sys.argv) > 2:
    cutoff = sys.argv[2]

hdulist = pyfits.open(filename)
hdu0 = hdulist[0]
hdu1 = hdulist[1]
#hdu2 = hdulist[2]
data1 = hdu1.data['data']
#data2 = hdu2.data
header1 = hdu1.header
#print hdu0.header
#print hdu1.header
fchannel = hdulist['SUBINT'].data[0]['DAT_FREQ']
fch1 = fchannel[0]
obsfreq = hdu0.header['OBSFREQ']
obsnchan = hdu0.header['OBSNCHAN']
obsbw = hdu0.header['OBSBW']
fmin = obsfreq - obsbw/2.
fmax = obsfreq + obsbw/2.
nf = obsnchan
df = hdu1.header['CHAN_BW']
tsamp = hdu1.header['TBIN']
nsubint = hdu1.header['NAXIS2']
samppersubint = int(hdu1.header['NSBLK'])
nsamp = nsubint * samppersubint
sourename = hdu0.header['SRC_NAME']
ra = hdu0.header['RA']
dec = hdu0.header['DEC']
#tstart = Decimal("%d.%d" % (hdu0.header['STT_IMJD'], hdu0.header['STT_SMJD']))
subintoffset = hdu1.header['NSUBOFFS']
tstart = "%.13f" % (Decimal(hdu0.header['STT_IMJD']) + Decimal(hdu0.header['STT_SMJD'] + tsamp * samppersubint * subintoffset )/secperday )
nbits = hdu0.header['BITPIX']
header = hdu0.header + hdu1.header


print 'ra:', ra, 'dec:', dec
print 'tsamp:', tsamp
print 'nsubint', nsubint
print 'duration:', tsamp * nsamp
print 'freq %s MHz, nchan %d, bw %s MHz' % ( obsfreq, obsnchan, obsbw)
print 'MJD:', tstart
freq_min = obsfreq - df * obsnchan / 2
chan_i = np.arange(obsnchan)
freq = freq_min + chan_i * df

data = np.squeeze(data1)
print 'data.shape', data.shape
k,l,m = data.shape
data = data.reshape((-1, m)).mean(axis=0)

print 'makezap took time:', time.time() - now
sig, nos = smooth(data, level=1)
allidx = np.arange(obsnchan)
badidx = allidx[np.abs(nos) > cutoff]
#goodidx = allidx[np.abs(nos) <= 0.1]
#from pylab import *
#plot(freq[goodidx], data[goodidx], 'b-')
#plot(freq, sig,  'y-')
#xlabel('frequency (MHz)')
#show()
#plot(freq, np.abs(nos))
#show()

zaplist = ','.join([str(i) for i in badidx])
fo = open('chans.zap', 'w')
fo.write(zaplist)
fo.close()
