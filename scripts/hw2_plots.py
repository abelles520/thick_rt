
# Author: Alex Belles
# Last updated: Jan 20, 2020

# This script creates a plot for the second HW assignment in Astro 530

import numpy as np
from thick_rt import planck
import matplotlib.pyplot as plt

plt.style.use('classic')

# problem 2, plot planck function for different T's over different range and axes scales

# range of 0 to 12 um^-1

wavenum_array = np.linspace(1e-8, 12, num=1000)

spec_int_3k = [planck.planck_wavenum(i, 3000) for i in wavenum_array]
spec_int_7k = [planck.planck_wavenum(i, 7000) for i in wavenum_array]
spec_int_10k = [planck.planck_wavenum(i, 10000) for i in wavenum_array]


# linear-linear
plt.plot(wavenum_array, spec_int_3k, 'r-', label='T = 3,000 K')
plt.plot(wavenum_array, spec_int_7k, 'y-', label='T = 7,000 K')
plt.plot(wavenum_array, spec_int_10k, 'b-', label='T = 10,000 K')
plt.xlabel(r'Wavenumber ($\mu$m$^{-1}$)')
plt.ylabel(r'Specific Intensity (erg/s/sr/cm$^2$/Hz)')
plt.legend()
plt.savefig('hw2_problem2_linlin.png', dpi=300)

# log-linear
plt.clf()
plt.plot(wavenum_array, spec_int_3k, 'r-', label='T = 3,000 K')
plt.plot(wavenum_array, spec_int_7k, 'y-', label='T = 7,000 K')
plt.plot(wavenum_array, spec_int_10k, 'b-', label='T = 10,000 K')
plt.xlabel(r'Wavenumber ($\mu$m$^{-1}$)')
plt.ylabel(r'Specific Intensity (erg/s/sr/cm$^2$/Hz)')
plt.legend(loc=3)
plt.yscale('log')
plt.savefig('hw2_problem2_loglin.png', dpi=300)

# log-log
plt.clf()
plt.loglog(wavenum_array, spec_int_3k, 'r-', label='T = 3,000 K')
plt.loglog(wavenum_array, spec_int_7k, 'y-', label='T = 7,000 K')
plt.loglog(wavenum_array, spec_int_10k, 'b-', label='T = 10,000 K')
plt.xlabel(r'Wavenumber ($\mu$m$^{-1}$)')
plt.ylabel(r'Specific Intensity (erg/s/sr/cm$^2$/Hz)')
plt.xlim([0.1, 12])
plt.legend(loc=3)
plt.savefig('hw2_problem2_loglog.png', dpi=300)
