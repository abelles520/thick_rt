

# Author: Alex Belles
# Last updated: Jan 15, 2020

# This script will have functions for the planck function. It is very possible
# that this script will get renamed at some point.

from .constants import *
import numpy as np

def planck_freq(nu, T):
    """
    Planck law function in terms of frequency
    """
    return (2*PLANCK_ERG*nu**3/SPEEDOFLIGHT**2)/(np.exp((PLANCK_ERG*nu)/(BOLTZMANN_ERG*T))-1)

def planck_wave(wave, T):
    """
    Planck law function in terms of wavelength
    """
    return (2*PLANCK_ERG*SPEEDOFLIGHT**2/wave**5)/(np.exp((PLANCK_ERG*SPEEDOFLIGHT)/(wave*BOLTZMANN_ERG*T))-1)
