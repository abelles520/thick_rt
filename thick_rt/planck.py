

# Author: Alex Belles
# Last updated: Jan 20, 2020

# This script will have functions for the planck function. It is very possible
# that this script will get renamed at some point.
# may refactor to include astropy units 

from .constants import *
import numpy as np

def planck_freq(nu, T):
    """
    Planck law function in terms of frequency

    returns in units of erg/s/cm^2/Hz
    """
    return (2*PLANCK_ERG*nu**3/SPEEDOFLIGHT**2)/(np.exp((PLANCK_ERG*nu)/(BOLTZMANN_ERG*T))-1)

def planck_wave(wave, T):
    """
    Planck law function in terms of wavelength

    input:
    wave - wavelength in angstroms
    T - temperature in K
    
    returns in units of erg/s/cm^2/A
    """
    return (1e8)**4*(2*PLANCK_ERG*SPEEDOFLIGHT**2/wave**5)/(np.exp((1e8*PLANCK_ERG*SPEEDOFLIGHT)/(wave*BOLTZMANN_ERG*T))-1)


def planck_wavenum(wavenum, T):
    """
    Planck law function in terms of wavenumber where wavenumber is defined to be
    \tilde{\nu} = 1/\lambda

    typically has units of 1/um

    Inputs:
    wavenum - wavenumber in 1/um
    T - temperature in K

    returns in units of ergs/s/cm^2/Hz
    """

    wave = 1/wavenum*1e4    # convert to wavelength in angstroms

    tmp = planck_wave(wave, T)

    # convert to frequency units so multiply by wave^2/c
    # don't forget 1e8 factor to convert speed of light to angstrom/s

    return tmp*wave**2/(1e8*SPEEDOFLIGHT)
