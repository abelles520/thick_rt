
# Author: Alex Belles
# Last updated: Feb 4, 2020

import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt
from thick_rt.integrate import trapezoidal

plt.style.use('atmospheres.mplstyle')

# problem 6

# part (a) familiarize yourself with expn func in scipy.special

# see documentation here:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.expn.html

# part (b) NUmerical integrate the area under the curve for n=1,2,3
# how close to the analytic result can you get
# what limits your precision?

# minimum float value in python 1e-307


e1 = trapezoidal(lambda x: sc.expn(1, x), 1e-100, 10, 100000)

print("Integral of E1:", e1)

e2 = trapezoidal(lambda x: sc.expn(2, x), 0, 200, 100000)

print("Integral of E2:", e2)

e3 = trapezoidal(lambda x: sc.expn(3, x), 0, 200, 100000)

print("Integral of E3:", e3)


# part (c) determining bounds and sampling

lower = [10**(-x) for x in range(1, 30)]
upper = [i for i in range(1, 100)]
sampling = [i for i in range(100,100000,100)]

e1_lower_array = [trapezoidal(lambda x: sc.expn(1, x), i, 10, 100000) for i in lower]

e1_upper_array = [trapezoidal(lambda x: sc.expn(1, x), 1e-9, i, 100000) for i in upper]

e1_sampling =  [trapezoidal(lambda x: sc.expn(1, x), 1e-9, 9, i) for i in sampling]


plt.plot(lower, e1_lower_array, 'b-', label=r'Exp$_1$')
plt.hlines(1, min(lower), max(lower), color='r', linestyle='-')
plt.xlabel('Lower limit')
plt.ylabel('Integration value')
plt.title('E1 lower limit')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.savefig('e1_lower_bounds.eps')

plt.clf()
plt.plot(upper, e1_upper_array, 'b-', label=r'Exp$_1$')
plt.hlines(1, min(upper), max(upper), color='r', linestyle='-')
plt.xlabel('upper limit')
plt.ylabel('Integration value')
plt.title('E1 Upper limit')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.savefig('e1_upper_bounds.eps')

plt.clf()
plt.plot(sampling, e1_sampling, 'b-', label=r'Exp$_1$')
plt.hlines(1, min(sampling), max(sampling), color='r', linestyle='-')
plt.xlabel('Sampling')
plt.ylabel('Integration value')
plt.title('E1 Sampling')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.savefig('e1_sampling.eps')

# calculate final values and percent error
#(analytic-numerical)/analytic


e1_final = trapezoidal(lambda x: sc.expn(1, x), 1e-9, 10, 100000)

print("Integral of E1:", e1_final)
print('Percent error:', (1-e1_final)/1)

e2_final = trapezoidal(lambda x: sc.expn(2, x), 0, 10, 100000)

print("Integral of E2:", e2_final)
print('Percent error:', (0.5-e2_final)/0.5)

e3_final = trapezoidal(lambda x: sc.expn(3, x), 0, 10, 100000)

print("Integral of E3:", e3_final)
print('Percent error:', ((1/3)-e3_final)/(1/3))
