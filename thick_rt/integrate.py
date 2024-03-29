
# Author: Alex Belles
# Last updated: Feb 5, 2020

# This script contains a basic trapezodial rule integrator

import numpy as np

def trapezoidal(f, a, b, n):
    """
    This function uses the trapezoidal rule to integrate basic functions

    Inputs:
    f - a python function to be integrated
    a - lower bound
    b - upper bound
    n - number of points to use in numeric integration

    Outputs:
    A single number cooresponding to the function integrated over the given bounds
    """
    # See this stack overflow:  https://stackoverflow.com/questions/21146540/trapezoidal-rule-in-python

    h = float(b-a)/n
    s = 0
    s += f(a)/2
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s*h

def trap_log(f, a, b, n):
    """
    This function uses the trapezoidal rule to integrate basic functions
    This function uses logarithmic spacing

    Inputs:
    f - a python function to be integrated
    a - lower bound
    b - upper bound
    n - number of points to use in numeric integration

    Outputs:
    A single number cooresponding to the function integrated over the given bounds
    """
    # See this stack overflow:  https://stackoverflow.com/questions/21146540/trapezoidal-rule-in-python

    return trapezoidal(lambda x: f(np.exp(x))*np.exp(x), np.log(a), np.log(b), n)