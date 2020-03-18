
# Author: Alex Belles
# Last updated: Feb 11, 2020

import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt
from thick_rt.integrate import trapezoidal, trap_log
from thick_rt.constants import *
from thick_rt.opacity import *

plt.style.use('atmospheres.mplstyle')

# tests that code is functioning properly

print(kappa_Hminus_bf(100, 10000, 10000))
print(kappa_Hminus_ff(100, 10000, 10000))
print(kappa_H_bf(100, 10000, 10000))
print(kappa_H_ff(100, 10000, 10000))
print(kappa(100, 10000, 10000))


# making plots

wave_array = np.arange(2000.0, 20100.0, 100)


opacity_a = [kappa(10**1.08, 5143, i) for i in wave_array]
def stim_term(wave, T):
    return (1-10**(-1.2398e4/wave*(5040/T)))
def phi_term(Pe, T):
    return 1/(1+phi('H', T)/Pe)


plt.figure(figsize=(8,6))
plt.plot(wave_array, np.array(opacity_a)/(10**1.08)*1e26, 'b-', label=r'$\kappa_{\rm tot}$')
plt.plot(wave_array, [kappa_Hminus_bf(10**1.08, 5143, i)*stim_term(i, 5143)*phi_term(10**1.08, 5143)/(10**1.08)*1e26 for i in wave_array], 'k--', label=r"$\kappa_{H^{-}_{\rm bf}}$")
plt.plot(wave_array, [kappa_Hminus_ff(10**1.08, 5143, i)*phi_term(10**1.08, 5143)/(10**1.08)*1e26 for i in wave_array], 'k:', label=r"$\kappa_{H^{-}_{\rm ff}}$")
plt.plot(wave_array, [kappa_H_bf(10**1.08, 5143, i)*stim_term(i, 5143)*phi_term(10**1.08, 5143)/(10**1.08)*1e26  for i in wave_array], 'k-.', label=r"$\kappa_{H_{\rm bf}}$")
plt.plot(wave_array, [kappa_H_ff(10**1.08, 5143, i)*stim_term(i, 5143)*phi_term(10**1.08, 5143)/(10**1.08)*1e26  for i in wave_array], 'k-', label=r"$\kappa_{H_{\rm ff}}$")
plt.xlabel(r'$\lambda$ ($\AA$)')
plt.ylabel(r'$\kappa_\nu/P_e \times 10^{-26}$ cm$^2$/neutral H ')
plt.title('Figure 8.5a')
plt.legend()
plt.savefig('opacity_a.eps')


# b
opacity_b =[kappa(10**1.77, 6429, i) for i in wave_array]

plt.figure(figsize=(8,6))
plt.plot(wave_array, np.array(opacity_b)/(10**1.77)*1e26, 'b-', label=r'$\kappa_{\rm tot}$')
plt.plot(wave_array, [kappa_Hminus_bf(10**1.77, 6429, i)*stim_term(i, 6429)*phi_term(10**1.77, 6429)/(10**1.77)*1e26 for i in wave_array], 'k--', label=r"$\kappa_{H^{-}_{\rm bf}}$")
plt.plot(wave_array, [kappa_Hminus_ff(10**1.77, 6429, i)*phi_term(10**1.77, 6429)/(10**1.77)*1e26 for i in wave_array], 'k:', label=r"$\kappa_{H^{-}_{\rm ff}}$")
plt.plot(wave_array, [kappa_H_bf(10**1.77, 6429, i)*stim_term(i, 6429)*phi_term(10**1.77, 6429)/(10**1.77)*1e26  for i in wave_array], 'k-.', label=r"$\kappa_{H_{\rm bf}}$")
plt.plot(wave_array, [kappa_H_ff(10**1.77, 6429, i)*stim_term(i, 6429)*phi_term(10**1.77, 6429)/(10**1.77)*1e26  for i in wave_array], 'k-', label=r"$\kappa_{H_{\rm ff}}$")
plt.xlabel(r'$\lambda$ ($\AA$)')
plt.ylabel(r'$\kappa_\nu/P_e \times 10^{-26}$ cm$^2$/neutral H ')
plt.title('Figure 8.5b')
plt.legend()
plt.savefig('opacity_b.eps')

# c
opacity_c =[kappa(10**2.5, 7715, i) for i in wave_array]

plt.figure(figsize=(8,6))
plt.plot(wave_array, np.array(opacity_c)/10**2.5*1e26, 'b-', label=r'$\kappa_{\rm tot}$')
plt.plot(wave_array, [kappa_Hminus_bf(10**2.5, 7715, i)*stim_term(i, 5143)*phi_term(10**2.5, 7715)/10**2.5*1e26 for i in wave_array], 'k--', label=r"$\kappa_{H^{-}_{\rm bf}}$")
plt.plot(wave_array, [kappa_Hminus_ff(10**2.5, 7715, i)*phi_term(10**2.5, 7715)/10**2.5*1e26 for i in wave_array], 'k:', label=r"$\kappa_{H^{-}_{\rm ff}}$")
plt.plot(wave_array, [kappa_H_bf(10**2.5, 7715, i)*stim_term(i, 7715)*phi_term(10**2.5, 7715)/10**2.5*1e26  for i in wave_array], 'k-.', label=r"$\kappa_{H_{\rm bf}}$")
plt.plot(wave_array, [kappa_H_ff(10**2.5, 7715, i)*stim_term(i, 7715)*phi_term(10**2.5, 7715)/10**2.5*1e26  for i in wave_array], 'k-', label=r"$\kappa_{H_{\rm ff}}$")
plt.xlabel(r'$\lambda$ ($\AA$)')
plt.ylabel(r'$\kappa_\nu/P_e \times 10^{-26}$ cm$^2$/neutral H ')
plt.title('Figure 8.5c')
plt.legend()
plt.savefig('opacity_c.eps')

# d
opacity_d =[kappa(10**2.76, 11572, i) for i in wave_array]

plt.figure(figsize=(8,6))
plt.plot(wave_array, np.array(opacity_d)/(10**2.76)*1e26, 'b-', label=r'$\kappa_{\rm tot}$')
plt.plot(wave_array, [kappa_Hminus_bf(10**2.76, 11572, i)*stim_term(i, 11572)*phi_term(10**2.76, 11572)/(10**2.76)*1e26 for i in wave_array], 'k--', label=r"$\kappa_{H^{-}_{\rm bf}}$")
plt.plot(wave_array, [kappa_Hminus_ff(10**2.76, 11572, i)*phi_term(10**2.76, 11572)/(10**2.76)*1e26 for i in wave_array], 'k:', label=r"$\kappa_{H^{-}_{\rm ff}}$")
plt.plot(wave_array, [kappa_H_bf(10**2.76, 11572, i)*stim_term(i, 11572)*phi_term(10**2.76, 11572)/(10**2.76)*1e26 for i in wave_array], 'k-.', label=r"$\kappa_{H_{\rm bf}}$")
plt.plot(wave_array, [kappa_H_ff(10**2.76, 11572, i)*stim_term(i, 11572)*phi_term(10**2.76, 11572)/(10**2.76)*1e26  for i in wave_array], 'k-', label=r"$\kappa_{H_{\rm ff}}$")
plt.xlabel(r'$\lambda$ ($\AA$)')
plt.ylabel(r'$\kappa_\nu/P_e \times 10^{-26}$ cm$^2$/neutral H ')
plt.title('Figure 8.5d')
plt.legend()
plt.savefig('opacity_d.eps')