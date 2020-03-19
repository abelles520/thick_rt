#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
sys.path.append("..")
from partition import *
from constants import *
from opacity import *

# need to calculate Pe as a function of T

def Pe_iter(T, Pgas):
    """
    A function to get the electron pressure using Gray's equation 9.8
    """
    
    df = pd.read_csv(r'..\aux_files\SolarAbundance.txt', sep='\t')
    df = df.dropna()
    df = df[(df['element'] != 'Li') & (df['element'] !='Cs')] 
    A_array = 10**(df['logA'].values)
    el_array = df['element']
    
    Pe_guess = min(Pgas/2.0, np.sqrt(Pgas*phi('H', T)))
    

    phi_array = np.array([phi(i, T) for i in el_array])
    
    # then iteratively solve for best Pe
    f = lambda P: P-Pgas*np.sum(A_array*(phi_array/P)/(1+phi_array/P))/np.sum(A_array*(1+(phi_array/P)/(1+phi_array/P)))
    
    return fsolve(f, Pe_guess)[0]
    





