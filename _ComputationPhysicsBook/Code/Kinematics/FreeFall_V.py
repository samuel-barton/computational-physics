#!/usr/bin/env python
# Program FreeFall_V.py
"""
This program uses the Euler method to solve for the motion of a ball
dropped from rest close to the surface of Earth. The program depends
on the function VelocityLinearDrag (contained in the file EulerFreeFall)
to execute the Euler method. 
"""
import sys, EulerFreeFall
import numpy as np
import matplotlib.pyplot as plt

#t=0.0		# initialize time to 0.0
g=9.8		# define acceleration due to gravity
#
# 	Now read the input from the terminal:
#	Format: python FreeFallLinearDrag 'outfile' v0 tmax dt
#
try:
	outfilename = sys.argv[1]
	v = float(sys.argv[2]) 	# initial velocity (+=down)
	vterminal=float(sys.argv[3]) # terminal velocity
	tmax = float(sys.argv[4])	# stop time
	dt = float(sys.argv[5])		# time step
except:
	print "Usage:", sys.argv[0], "outfile vinitial vterminal tmax dt"
	sys.exit(1)
	
outfile = open(outfilename, 'w')	# open file for writing			

# Main calculation loop
t = np.arange(0.0, tmax + dt, dt)
vel = np.zeros(t.size) # t.size returns the length of the numpy t array
vel[0] = v 
for i in range(1, t.size) :
    vel[i] = EulerFreeFall.VelocityLinearDrag(vel[i-1], dt, 9.8, vterminal)

# write data arrays to a file using numpy:
# (np.c_ forces arrays to be written as columns)

np.savetxt(outfilename, np.c_[t,vel], fmt = '%10.3f %10.3f', delimiter='\t' , header = 'time (s) \t speed (m/s)')

# create array for plot of analytic function for comparison:
analytic = vterminal*(1-np.exp(-g*t/vterminal))
plt.plot(t, analytic,'k--')
# read in the datafile, & plot it with MatPlotLib:	
data = np.loadtxt(outfilename, skiprows=0)	# (numpy function)
xaxis = data[ : , 0 ]			# first column
yaxis = data[ : , 1 ]			# second column
#plt.ylim(0.0, 0.21)
plt.plot( xaxis, yaxis, marker='.', markersize=5, linestyle='None')
plt.legend(('Analytic Solution', 'Euler Method'), loc='best') # writes legend
plt.xlabel('time (s)', fontsize = 18)
plt.ylabel('velocity (m/s)', fontsize = 18)
plt.title('Vertically Dropped Ball', fontsize = 18)
plt.show()

