import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0.2,2.2,0.2) # creates array of points
temp=np.array([8.24,  13.77,  17.47,  19.95, 21.62,  22.73,  
23.47,  23.98 , 24.32,  24.54])
tempError=([0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.1])
plt.errorbar(t,temp,xerr = 0.2, yerr=tempError, fmt='o') 
# fmt = 'o' plots points only (with no line connecting points)
plt.ylim(0.0,25.0)
plt.xlabel('time (s)', fontsize=16)
plt.ylabel('temperature (C)', fontsize=16)
plt.show()