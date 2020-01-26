
# Author: Alex Belles
# Last updated: Jan 23rd, 2020


from thick_rt.integrate import trapezoidal
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('atmospheres.mplstyle')

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



def contribution(func, tau, a):
    """
    Takes a source function and tau to create the contribution function that can be 
    integrated to get the emergent intensity
    """
    return func(tau, a)*np.exp(-tau)


a_array = [1,1,1]

lin_val = trapezoidal(lambda x: contribution(linear_source, x, a_array), 0, 100, 100)
quad_val = trapezoidal(lambda x: contribution(quadratic_source, x, a_array), 0, 100, 100)

print("Bounds from 0 to 100, 100 trapezoids \n")

print("Emergent intensity, linear:", lin_val, '\n')
print(r"Linear source function at $\tau=1$:", linear_source(1, a_array), '\n\n')
print("Emergent intensity, quadratic:", quad_val, '\n')
print(r"Quadratic source function at $\tau=1$:", quadratic_source(1, a_array), '\n\n')

tau_array = np.linspace(0, 10, 100)

fig = plt.figure(figsize=(10,6))

plt.plot(tau_array, linear_source(tau_array, a_array), 'b-', label='Linear source')
plt.plot(tau_array, contribution(linear_source, tau_array, a_array), 'b--', label='Linear Contribution function')
plt.plot(tau_array, quadratic_source(tau_array, a_array), 'r-', label='Quadratic source')
plt.plot(tau_array, contribution(quadratic_source, tau_array, a_array), 'r--', label='Quadratic contribution function')
plt.xlabel(r'$\tau$')
plt.ylabel("Intensity")
plt.yscale("log")
plt.legend()
plt.savefig('contribution_function.eps', format='eps', dpi=1000)

# look at approaching analytic result as a function of lower, upper bounds, and number of trapezoids

trap_array = np.arange(1, 1000, 10)

lin_val_trap = [trapezoidal(lambda x: contribution(linear_source, x, a_array), 0, 100, i) for i in trap_array]
quad_val_trap = [trapezoidal(lambda x: contribution(quadratic_source, x, a_array), 0, 100, i) for i in trap_array]

upper_array = np.arange(1,200,2)
lin_val_upper = [trapezoidal(lambda x: contribution(linear_source, x, a_array), 0, i, 200) for i in upper_array]
quad_val_upper = [trapezoidal(lambda x: contribution(quadratic_source, x, a_array), 0, i, 200) for i in upper_array]

plt.clf()
fig = plt.figure(figsize=(10,6))

plt.plot(trap_array, lin_val_trap, 'b-', label='Linear source')
plt.plot(trap_array, quad_val_trap, 'r-', label='Quadratic source')
plt.hlines(2, min(trap_array), max(trap_array), colors='b', linestyles='dashed')
plt.hlines(4, min(trap_array), max(trap_array), colors='r', linestyles='dashed')
plt.xlabel("Number of trapezoids")
plt.ylabel("Numerical Value")
plt.xscale('log')
plt.yscale("log")
#plt.title("Numerical integration value as function of number of trapezoids")
plt.legend()
plt.savefig('trapezoids.eps', format='eps', dpi=1000)

plt.clf()
fig = plt.figure(figsize=(10,6))

plt.plot(upper_array, lin_val_upper, 'b-', label='Linear source')
plt.plot(upper_array, quad_val_upper, 'r-', label='Quadratic source')
plt.hlines(2, min(upper_array), max(upper_array), colors='b', linestyles='dashed')
plt.hlines(4, min(upper_array), max(upper_array), colors='r', linestyles='dashed')
plt.xlabel("Upper bound")
plt.ylabel("Numerical Value")
plt.xscale('log')
plt.yscale("log")
#plt.title("Numerical integration value as function of upper bound")
plt.legend()
plt.savefig('upperbound.eps', format='eps', dpi=1000)
