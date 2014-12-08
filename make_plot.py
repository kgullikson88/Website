import HelperFunctions
import matplotlib.pyplot as plt
import numpy as np
import FittingUtilities
import os

home = os.environ['HOME']
filedir = '{:s}/School/Research/IGRINS_data/20141014/'.format(home)

# Read the orders
original_orders = HelperFunctions.ReadExtensionFits('{:s}HIP_109056.fits'.format(filedir))
corrected_orders = HelperFunctions.ReadExtensionFits('{:s}HIP_109056_telluric_corrected.fits'.format(filedir))

# Get the appropriate one
original = original_orders[33]
corrected = corrected_orders[33]

# Redo the continuum
c = FittingUtilities.Continuum(corrected.x, corrected.y, fitorder=3, lowreject=2, highreject=5)
original.cont = np.r_[c[0], c, c[-1]]
corrected.cont = c

# Make the figure
fig = plt.figure()
fig.subplots_adjust(hspace=0.0)
top = fig.add_subplot(211)
bottom = fig.add_subplot(212)
top.set_xticklabels([])

# Plot
top.plot(original.x, original.y/original.cont, 'k-')
bottom.plot(corrected.x,  corrected.y/corrected.cont, 'k-')

# Annotate
top.text(2175, 1.05, 'Before Correction', color='red', fontsize=15)
bottom.text(2175, 1.02, 'After Correction', color='green', fontsize=15)

# Play with formatting
top.set_ylim((0.55, 1.15))
top.set_xlim((2157, 2184))
bottom.set_xlim((2157, 2184))

# Labels
bottom.set_xlabel('Wavelength (nm)', fontsize=15)
fig.text(0.05, 0.5, 'Normalized Flux', ha='center', va='center', rotation='vertical', fontsize=15)

plt.show()