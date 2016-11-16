import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c

t = np.linspace(0,4,50)
temp = fitFunc(t, 5.0, 1.5, 0.5)
noisy = temp + 0.25*np.random.normal(size=len(temp))
fitParams, fitCovariances = curve_fit(fitFunc, t, noisy)
print fitParams
print fitCovariances

plt.ylabel('Temperature (C)', fontsize = 16)
plt.xlabel('time (s)', fontsize = 16)
plt.xlim(0,4.1)
# plot the data as red circles with errorbars in the vertical direction
plt.errorbar(t, noisy, fmt = 'ro', yerr = 0.2)
# now plot the best fit curve and also +- 3 sigma curves
# the square root of the diagonal covariance matrix element 
# is the uncertianty on the corresponding fit parameter.
sigma = [fitCovariances[0,0], fitCovariances[1,1], fitCovariances[2,2] ]
plt.plot(t, fitFunc(t, fitParams[0], fitParams[1], fitParams[2]),\
         t, fitFunc(t, fitParams[0] + 3*sigma[0], fitParams[1] - 3*sigma[1], fitParams[2] + 3*sigma[2]),\
         t, fitFunc(t, fitParams[0] - 3*sigma[0], fitParams[1] + 3*sigma[1], fitParams[2] - 3*sigma[2])\
         )

# save plot to a file
savefig('dataFitted.pdf', bbox_inches=0, dpi=600)