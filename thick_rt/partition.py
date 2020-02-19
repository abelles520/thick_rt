
# Author: Alex Belles
# Last updated: February 19th, 2020

import numpy as np
import pandas as pd


def partition(ion_name, T):
    """
    Using the partit.txt in aux_files, interpolate the given temperature
    to get the correct value of the partition function
    
    if ion_name is H+ or H-, the known value is returned without interpolation

    """
    if ion_name in ['H+', 'H-']:
        return 1.0
    df = pd.read_csv('../aux_files/partit.txt', delim_whitespace=True, header=None,  na_values='-')
    df.columns = ['name', 0.2, 0.4, 0.6 ,0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 'log g0']
    
    row = df[df['name']==ion_name]
    theta_array = np.array([0.2, 0.4, 0.6 ,0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
    log_u = row.values[0][1:-1].astype(float)
    theta = 5040/T
    
    if theta>2.0 or theta<0.2:
        print('out of bounds')
        return np.nan
    
    return 10**np.interp(theta, theta_array, log_u)