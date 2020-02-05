
# Author: Alex Belles
# Date modified: Feb 5th, 2020

# this file contains functions for the moments of intensity

import numpy as np
import scipy.special as sc
from .integrate import *

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