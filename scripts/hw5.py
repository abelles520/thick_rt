
# Author: Alex Belles
# Last updated: Feb 11, 2020

import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt
from thick_rt.integrate import trapezoidal, trap_log
from thick_rt.moments import *

plt.style.use('atmospheres.mplstyle')

# Problem 9

# part b

# array of wavenumbers in inverse um
wavenum_array = np.linspace(1e-8, 12, num=1000)

# array of wavelengths in angstroms 
wave_array = 1/wavenum_array*1e4

# array of frequencies in Hz 
freq_array = 3e18/wave_array

Teff = 8700  # in K

"""
curly_F0 = [4*np.pi*eddington_flux_0_grey(Teff, i) for i in freq_array]

EB_approx = [np.pi*planck_freq(i, Teff) for i in freq_array]

plt.plot(wavenum_array, curly_F0, 'b-', label=r"$\mathcal{F}_{\nu}(0)$")
plt.plot(wavenum_array, EB_approx, 'r-', label=r"E-B approx.")
plt.xlabel(r'Wavenumber ($\mu$m$^{-1}$)')
plt.ylabel(r'Intensity (erg/s/cm$^2$/Hz)')
#plt.xscale('log')
plt.yscale('log')
plt.ylim([10**(-9), 10**(-3)])
plt.legend()
plt.savefig('problem9_c.eps')

error_array = [(i-j) for i,j in zip(curly_F0, EB_approx)]

plt.clf()
plt.plot(wavenum_array, error_array, 'r-', label='Difference')
plt.xlabel(r'Wavenumber ($\mu$m$^{-1}$)')
plt.ylabel('Error')
plt.legend()
plt.savefig('problem9_d_difference.eps')

# calculate d2S/dtau^2 at tau=1 for all wavelengths 

tau_array = np.linspace(0.95, 1.05, num=100)
derivative_array = []

for freq in freq_array:
    # calculate the source function at all values of tau_array
    s_array = np.array([planck_freq(freq, Teff*(0.5+ 3/4*t)**(1/4)) for t in tau_array])
    delta_tau = tau_array[1]-tau_array[0]
    # calculate differences and divide by delta tau
    diff = np.diff(s_array)
    d1_array = diff/delta_tau
    # repeat to get second derivative 
    diff2 = np.diff(d1_array)
    d2_array = diff2/delta_tau
    der = d2_array[int(len(d2_array)/2)]
    # append derivative to array 
    derivative_array.append(der)


plt.clf()
plt.plot(wavenum_array, derivative_array, 'b-', label=r'$\frac{d^2S_\nu}{d\tau^2}$')
plt.plot(wavenum_array, error_array, 'r-', label='Difference')
plt.plot(wavenum_array, np.array(error_array)*(np.pi*5/18), 'k--', label=r'5$\pi$/18 $(\mathcal{F}_{\nu}(0)-\pi B_{\nu}(T_{\rm eff}))$')
plt.xlabel(r'Wavenumber ($\mu$m$^{-1}$)')
#plt.ylabel('Error or second derivative')
plt.legend()
plt.savefig('problem9_d_factor.eps')

# offset factor between derivative and difference
# see picture for true offset factor

print(5/6)
print(max(error_array)/max(derivative_array))
"""

# problem 10

tau_array = np.linspace(0.01, 50, 1000)

eddington_flux_array = [curly_F_tau(Teff, t) for t in tau_array]

plt.plot(tau_array, eddington_flux_array, 'b-', label=r"$\mathcal{F}(\tau)$")
plt.xlabel(r'$\tau$')
plt.ylabel("Flux (intensity cgs units)")
plt.show()
