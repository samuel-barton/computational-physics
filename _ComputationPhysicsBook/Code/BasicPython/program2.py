#!/usr/bin/env python
# Program 2
"""
Usage:  python program2.py outfile v0 t dt
This program computes and plots the position vs time for a projectile
launched upward from the surface of Earth. Assumptions: zero air 
resistance; small initial velocity so that the variation 
of g with height can be neglected. This program uses the simple 1d 
kinematic equations to calculate the height as a function of time. 
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

g=9.8		# acceleration at Earth's surface in m/s^2
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

def height(v0,t):
	if t==0 and v0<0.0: 
		print "initial velocity must be >= 0"
		sys.exit(1)
	elif (v0*t-0.5*g*t**2) >=0.0: 
		return v0*t-0.5*g*t**2
	else:
		print "ball has hit the ground"
		return 0.0
			
# Write Header line as first row in data file
outfile.write('time (s) \t height (m) \n')	

# Main calculation loop
imax = int(tmax/dt)
for i in range(imax+1):
	t=i*dt
	y = height(v0,t)
	outfile.write('%g \t %g\n' % (t,y))
outfile.close()

# read in the datafile, & plot it with MatPlotLib:	
data = np.loadtxt(outfilename, skiprows=1)	# (numpy function)
xaxis = data[ : , 0 ]			# first column
yaxis = data[ : , 1 ]			# second column
plt.plot( xaxis, yaxis, marker='o', linestyle='None')
plt.xlabel('time (s)')
plt.ylabel('Height (m)')
plt.title('Vertically Launched Ball')
plt.show()

