#!/usr/bin/env python
# Program Falling Ball
"""
This program uses the Euler method to solve for the motion of a ball
dropped from rest close to the surface of Earth. The program depends
on the function VelocityLinearDrag (contained in the file EulerFreeFall)
to execute the Euler method. 
"""
import sys, EulerFreeFall
from pylab import *
t=0.0		# initialize time to 0.0
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
# Write Header line as first row in data file
outfile.write('time (s) \t speed \n')	
outfile.write('%g \t %g\n' % (t,v))
# Main calculation loop
imax = int(tmax/dt)
for i in range(imax+1):
	t=i*dt
	v = EulerFreeFall.VelocityLinearDrag(v, dt, 9.8, vterminal)
	outfile.write('%g \t %g\n' % (t,v))
outfile.close()
# create array for plot of analytic function for comparison:
a = arange(0,tmax,dt)
c = vterminal*(1-exp(-g*a/vterminal))
plot(a,c,'k--')
# read in the datafile, & plot it with MatPlotLib:	
data = load(outfilename, skiprows=1)	# (pylab function)
xaxis = data[ : , 0 ]			# first column
yaxis = data[ : , 1 ]			# second column
plot( xaxis, yaxis, marker='.', markersize=5, linestyle='None')
legend(('Analytic Solution', 'Euler Method'), loc='best') # writes legend
xlabel('time (s)')
ylabel('velocity (m/s)')
title('Vertically Dropped Ball')
show()

