#!/usr/bin/env python
# Program Falling Ball
"""
This program uses the Euler method to solve for the motion of a ball
dropped from rest close to the surface of Earth. The program depends
on the function VelocityLinearDrag to execute the Euler method. 
"""
import sys, getopt, EulerFreeFall
from pylab import *
t=0.0		# initialize time to 0.0
g=9.8		# define acceleration due to gravity
#
#	READ IN RUN PARAMETERS (new method; GETOPT)
#
options, timeSteps = getopt.getopt(sys.argv[1:],
 'hf:v:t:m:',['help','filename=', 'v_initial=', 'v_terminal=', 'tmax='])
for option, value in options:
	if option in ('-h', '--help'):
		print "python sys.argv[0] --filename --v_initial \
		 --v_terminal --tmax dt0 dt1..."; sys.exit(0)
	elif option in ('-f', '--filename'):
		filename=value
	elif option in ('-v','--v_initial'):
		v=float(value)
		vinitial=v
	elif option in ('-t', '--v_terminal'):
		vterminal = float(value)
	elif option in ('-m','--tmax'):
		tmax = float(value)
print filename, v, vterminal, tmax
#Now loop over all values of dt...
for n in timeSteps:
	dt=float(n)	# change string to floating point number. 
	print dt
	fname=filename+str(n)+'.dat'
	outfile=open(fname, 'w')	# open file for writing			
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
# read in the datafile, & plot it with MatPlotLib:	
	data = load(fname, skiprows=1)	# (pylab function)
	xaxis = data[ : , 0 ]			# first column
	yaxis = data[ : , 1 ]			# second column
	plot( xaxis, yaxis, marker='.', markersize=7, linestyle='None')
	t=0.0
	i=0
	v=vinitial

# set up legend, label axes and show plot:
legendstr=[]	#the following four lines set up the legend 
for j in range(len(timeSteps)):
	legendstr.append('dt=' + timeSteps[j])
legendstring=str(legendstr[:])
legendstring=legendstring.strip("[ ]")
print legendstring
legend(legendstring.split(', '), loc='best') # writes legend
xlabel('time (s)')
ylabel('velocity (m/s)')
title('Vertically Dropped Ball')
show()

