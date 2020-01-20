
# Author: Alex Belles
# Last updated: Jan 15th, 2020

# This script creates a plot for the first HW assignment in Astro 530

import numpy as np
from thick_rt import planck
import matplotlib.pyplot as plt

plt.style.use('classic')

# use planck function to plot blackbody spectrum with solar effective temperature
# overplot with solar spectrum to show same area under the curve

data = np.loadtxt('solarspec_wehrli85.txt', skiprows=2, unpack=True)

#multiply nm by 10 to get Angstroms and specific flux by 100 to get cgs units

wave = 10*data[0]


sp_flux_pl = [6e-5*planck.planck_wave(i, 5900) for i in wave]

plt.plot(wave, 100*data[1], 'b-', label='Solar spectrum')
plt.plot(wave, sp_flux_pl, 'r-', label='Planck Law for T=5900 K', lw=2)
plt.xlabel(r'Wavelength ($\AA$)')
plt.xlim([1.5e3, 3e4])
plt.ylabel('Specific flux (Arb. Units)')
plt.xscale('log')
plt.legend()
plt.savefig('hw1_plot_solar_spec_color_temp.png', dpi=300)

