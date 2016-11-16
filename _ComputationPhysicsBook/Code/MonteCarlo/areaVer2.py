"""
program area.py
this code calculates the area under y=x**2 between x=0 and x=1
by using a monte carlo technique.

"""
from  MonteCarlo import monteCarloDarts
from functions import *
import numpy as np
import matplotlib.pyplot as plt

nThrows = np.arange(10000, 1000000, 10000)
area = []
for n in nThrows:
    area.append(monteCarloDarts( n, f))


plt.plot(nThrows, area)
plt.xlabel('Number of darts thrown')
plt.ylabel('Area')
plt.show()



#print "Area estimate after %g throws is = %g" % (nThrows, area)
