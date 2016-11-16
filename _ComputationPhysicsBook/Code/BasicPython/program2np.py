#!/usr/bin/env python
# Program 2np
"""
Useage:   python program2np.py outfilename v0 tmax dt
     
This program computes and plots the position vs time for a projectile
launched upward from the surface of Earth. Assumptions: zero air 
resistance; small initial velocity so that the variation 
of g with height can be neglected. This code uses numerical python
to calculate the vertical height, instead of using python to loop over 
points one at a time using a for loop.    
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

g=9.8		# acceleration at Earth's surface in m/s^2
#
# 	Now read the input from the terminal:
#	Format: python program2.py 'outfile' v0 tmax dt
#
try:
	outfilename = sys.argv[1]
	v0 = float(sys.argv[2]) 	# initial velocity (+=up)
	tmax = float(sys.argv[3])	# stop time
	dt = float(sys.argv[4])		# time step
except:
	print "Usage:", sys.argv[0], "outfile v0 t dt"
	sys.exit(1)

# Main calculation using numpy arrays
t = np.arange(0.0, tmax, dt) 
y = v0*t-0.5*g*t**2

# write data arrays to a file using numpy:
# (np.c_ forces arrays to be written as columns)

np.savetxt(outfilename, np.c_[t,y], fmt = '%.3f', delimiter='\t' ) 

# read in the datafile, & plot it with MatPlotLib:	
data = np.loadtxt(outfilename, skiprows=1)	# (pylab function)
xaxis = data[ : , 0 ]			# first column
yaxis = data[ : , 1 ]			# second column
plt.plot( xaxis, yaxis, marker='o', color = 'r', linestyle='None')
plt.xlabel('time (s)')
plt.ylabel('Height (m)')
plt.title('Vertically Launched Ball')
plt.show()