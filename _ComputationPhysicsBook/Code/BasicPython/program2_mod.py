#!/usr/bin/env python
# Program 2 Modified
"""
This program computes and plots the position vs time for a projectile
launched upward from the surface of Earth. Assumptions: zero air 
resistance;  small initial velocity so that the variation of g with 
height can be neglected.
Modifications: 
07/30/2007: Modified code to have the analytic height calculation 
performed in a separate file called analytic.py . 
"""
import sys, analytic
import numpy as np
import matplotlib.pyplot as plt

t=0.0		# initialize time to 0.0
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
	
outfile = open(outfilename, 'w')	# open file for writing			
# Write Header line as first row in data file
outfile.write('time (s) \t height (m) \n')	

# Main calculation loop
imax = int(tmax/dt)
for i in range(imax+1):
	t=i*dt
	y = analytic.height(v0,t)
	outfile.write('%g \t %g\n' % (t,y))
outfile.close()

# read in the datafile, & plot it with MatPlotLib:	
data = np.loadtxt(outfilename, skiprows=1)	# (pylab function)
xaxis = data[ : , 0 ]			# first column
yaxis = data[ : , 1 ]			# second column
plt.plot( xaxis, yaxis, marker='o', linestyle='None')
plt.xlabel('time (s)')
plt.ylabel('Height (m)')
plt.title('Vertically Launched Ball')
plt.show()

