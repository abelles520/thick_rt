
# Author: Alex Belles
# last updated: Feb 21st, 2020

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from partition import *
from constants import *


def phi(ionized_ion, T):
    """
    Calculates the phi function from Gray's eqs 1.20-1.21
    
    T - is the temperature in K
    ionized_ion - is the name of the lower ionization state
    """
    
    theta = 5040/T
    if ionized_ion=='H-':
        u1 = partition('H', T)
        u0 = partition(ionized_ion, T)
        xi = 0.754195 # eV
    else:
        u1 = partition(ionized_ion+'+', T)
        u0 = partition(ionized_ion, T) 
        ionization_file = pd.read_csv("c:\\users\\belles\\documents\\courses\\530\\thick_rt\\thick_rt\\aux_files\\nist_ioniz.txt", delim_whitespace=True, header=None)
        ionization_file.columns = ['Z', 'name', 'mass', 'ioniz_e']
        row = ionization_file[ionization_file['name']==ionized_ion]
        xi = row['ioniz_e'].values[0]
    
    return 1.2020e9*u1/u0*theta**(-5/2)*10**(-theta*xi)
    
    
def kappa_Hminus_bf(Pe, T, wave):
    """
    Following equation 8.11-12 in Gray
    wave in angstroms
    T in kelvin
    Pe in cgs? dynes/cm^2
    """
    alpha_bf = 1.99654 - 1.18267e-5*wave + 2.64243e-6*wave**2 - 4.40524e-10*wave**3 + 3.23992e-14*wave**4 - 1.39568e-18*wave**5 + 2.78701e-23*wave**6
    theta = 5040/T
    if wave<1000 or wave>16200:
        return 0
    return 10**-18 * 4.158e-10 * alpha_bf * Pe * theta**(5/2) * 10**(0.754*theta)


def kappa_Hminus_ff(Pe, T, wave):
    """
    Following equation 8.13 in Gray
    """
    f0 = -2.2763-1.6850*np.log10(wave)+0.76661*(np.log10(wave))**2-0.053346*(np.log10(wave))**3
    f1 = 15.2827-9.2846*np.log10(wave)+1.99381*(np.log10(wave))**2-0.142631*(np.log10(wave))**3
    f2 = -197.789+190.266*np.log10(wave)-67.9775*(np.log10(wave))**2+10.6913*(np.log10(wave))**3-0.625151*(np.log10(wave))**4
    theta = 5040/T
    return 1e-26*Pe*10**(f0+f1*np.log10(theta)+f2*(np.log10(theta))**2) 


def g_bf(n, T, wave):
    """
    equation 8.6 in gray
    """
    return 1-(0.3456)/(wave*1.0968e-3)**(1/3)*(wave*1.0968e-3/(n**2)-1/2)


def kappa_H_bf(Pe, T, wave):
    """
    Using equations 8.4, 8.5, 8.8
    """
    # find n0
    n0 = int(np.floor(np.sqrt(13.6*EV_TO_ERG/(PLANCK_ERG*SPEEDOFLIGHT/(wave*1e-8)))))+1

    theta = 5040/T
    n_array = np.array([n0, n0+1, n0+2])
    alpha0 = 1.0449e-26
    I = 13.6    # eV
    xi_array = I*(1-(1/((n_array)**2)))
    g_array = np.array([g_bf(i, T, wave) for i in n_array])
    summation = sum(g_array/(n_array**3)*10**(-theta*xi_array))
    xi3 = I*(1-1/((n0+3)**2)) 
    
    return alpha0*wave**3*(summation+(np.log10(np.e)/(2*theta*I))*(10**(-xi3*theta)-10**(-I*theta)))


def kappa_H_ff(Pe, T, wave):
    """
    Using equations 8.6, 8.10
    """
    R = 1.0968e-3  # inverse Angstroms
    theta = 5040/T
    g_ff = 1+0.3456/(wave*R)**(1/3)*(np.log10(np.e)/(theta*1.2398e4/wave)+0.5)
    alpha0 = 1.0449e-26
    I = 13.6 # in eV
    return alpha0*wave**3*g_ff*np.log10(np.e)/(2*theta*I)*10**(-theta*I)


def kappa_e(Pe, Pgas, A_array):
    """
    calculate the opacity due to electron scattering using equations
    8.17
    """
    sigma_T = 6.65e-25 #cm^2/electron
    sum_A = np.sum(A_array)
    return sigma_T*Pe/(Pgas-Pe)*sum_A


def kappa(Pe, Pgas, T, wave, A_array):
    """
    equation 8.18
    """
    theta = 5040/T
    return ((kappa_H_bf(Pe, T, wave) + kappa_H_ff(Pe, T, wave) + kappa_Hminus_bf(Pe, T, wave))*(1-10**(-1.2398e4/wave*theta)) + kappa_Hminus_ff(Pe, T, wave))*1/(1+phi('H', T)/Pe)+kappa_e(Pe, Pgas, A_array)






