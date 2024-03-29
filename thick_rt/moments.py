
# Author: Alex Belles
# Date modified: Feb 5th, 2020

# this file contains functions for the moments of intensity

import numpy as np
import scipy.special as sc
from .integrate import *
from .planck import *

def linear_source(tau, a):
    """
    Assume that the source function is linear with a_n=1 for n=0,1
    """

    return a[0]+a[1]*tau

def quadratic_source(tau, a):
    """
    Assume that the source function is quadratice with a_n=1 for n=0-2
    """

    return a[0] + a[1]*tau + a[2]*tau**2

def H_0_src(src_func, a_array, tau_array):
    """
    given an array of optical depths, the emergent H is calculated
    This is calculated assuming a given source function and using the exp int
    Also assume no incident radiation

    src_func: a function for the source function
    a_array: an array containing the a_n coeficients for the source function
    tau_array: an array of tau values to use for the integration
               (in reality, only the max and min values and the number of points)
    """
    min_tau = min(tau_array)
    sampling = len(tau_array)
    max_tau = max(tau_array)
  
    return 0.5*trap_log(lambda t: src_func(t, a_array)*sc.expn(2, t), min_tau,
                        max_tau, sampling)

def H_0_mu(src_func, a_array):
    """
    calculate emergent H given source function, approximating I as S
    Assuming no indicient radiation    
    """

    return 0.5*trapezoidal(lambda mu: src_func(mu, a_array)*mu, 0, 1, 10000)


def eddington_flux_0_grey(Teff, nu):
    """
    Calculate the emergent Eddington flux, curly F, under the grey approximation
    This function is similar to the H_0_mu function except the source function
    is the planck function at a given Teff.

    Based on the given Teff, the emergent eddington flux is calculated at the
    given frequency.

    curly F is returned in units of intensity (ergs/s/cm^2/Hz) 
    """

    min_tau = 1e-10
    max_tau = 20
    sampling = 2000
    
    return 0.5*trap_log(lambda t: planck_freq(nu, Teff*(0.5+ 3/4*t)**(1/4))*sc.expn(2, t), min_tau,
                        max_tau, sampling)


def curly_F_tau(Teff, tau):
    """
    Function for problem 10 
    calculates the eddington flux at a given tau
    NOTE this is not a F_\nu, assumes a planckian source function
    """

    return 2*np.pi*(trapezoidal(lambda t: integrated_planck(Teff*(0.5+ 3/4*t)**(1/4))*sc.expn(2, t-tau), tau, 20, 5000)-trapezoidal(lambda t: integrated_planck(Teff*(0.5+ 3/4*t)**(1/4))*sc.expn(2, tau-t), 0, tau, 5000))
