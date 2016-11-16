#!/usr/bin/env python
# Program Falling Ball
"""
This program uses the Euler method to solve for the motion of a ball
launched with an initial velocity v and angle theta. The program depends 
on the function VelocityLinearDrag to execute the Euler method. 
"""
import sys, verticalMotion
from pylab import *
#from numpy import *
from optparse import OptionParser
t=0.0		# initialize time to 0.0
g=9.8		# define acceleration due to gravity
#
#	READ IN RUN PARAMETERS (new method; optparse)
#	and Define variables needed
parser = OptionParser()
# define all options:
parser.add_option('-f', '--filename', dest='filename', type='string',
 help='filename for output', default='junk')
parser.add_option('-v', '--v_initial', dest='v', type='float', 
help='initial velocity', default=50.0)
parser.add_option('-o', '--angle', dest='angle', type='float', 
help='initial launch angle', default=45.0)
parser.add_option('-x', '--x_initial', dest='x', type='float', 
help='initial x position', default=0.0)
parser.add_option('-y', '--y_initial', dest='y', type='float', 
help='initial y position', default=0.0)
parser.add_option('-t', '--v_terminal', dest='vterminal', type='float',
help='terminal velocity', default=30.0)
parser.add_option('-m', '--tmax', dest='tmax', type='float', 
help='maximum simulation time', default=20.0)
parser.add_option('-a', '--dt', dest='dt', 
help='time steps', action = 'append')	# the append action makes a list. 

#now read from command line 
option, args = parser.parse_args(sys.argv[1: ])
#define the variables we need 
filename=option.filename
v=option.v 	# sets initial velocity 
vinitial = v	#save initial velocity for later use (for multiple runs)
angle=option.angle*pi/180.0 # convert launch angle to radians. 
vx=v*cos(angle)
vy=v*sin(angle)
#velocity=([vx,vy])
x = option.x
y = option.y
xinitial = x
yinitial = y
vterminal = option.vterminal
tmax = option.tmax
timeSteps=option.dt	# saves dt values as a string list called timeSteps
print filename, v, vterminal, tmax, timeSteps
#
# Main Loop: 
for n in timeSteps:
	dt=float(n)# need to convert string into a floating point number.
	fname=filename+str(n)+'.dat'
	outfile=open(fname, 'w')	# open file for writing			
	# Write Header line as first row in data file
	outfile.write('time (s) \t x (m) \t y (m)\t vx (m/s) \t vy (m/s)\n ')	
	outfile.write('%g \t %g\t %g \t %g \t %g\n' % (t, x, y, vx, vy))
	# Main calculation loop
	imax = int(tmax/dt)
	for i in range(imax+1):
		t=i*dt
		vx = verticalMotion.XVelocityQD(v, vx, dt, 9.8, vterminal)
		vy = verticalMotion.YVelocityQD(v, vy, dt, 9.8, vterminal)
		x = verticalMotion.PositionQD(x, vx, dt)
		y = verticalMotion.PositionQD(y, vy, dt)
		v = vx*vx + vy*vy
		outfile.write('%g \t %g\t %g \t %g \t %g\n' % (t, x, y, vx, vy))
		
	outfile.close()
	data = load(fname, skiprows=1)	# (pylab function)
	xaxis = data[ : , 1 ]			# first column
	yaxis = data[ : , 2 ]			# second column
	plot( xaxis, yaxis, marker='.', markersize=7, linestyle='None')
	t=0.0
	i=0
	v=vinitial

# set up plot parameters and plot data
legendstr=[]	#the following four lines set up the legend 
for j in range(len(timeSteps)):
	legendstr.append('dt=' + timeSteps[j])
legendstring=str(legendstr[:])
legendstring=legendstring.strip("[ ]")
print legendstring
legend(legendstring.split(', '), loc='best') # writes legend
xlabel('x (m)')
ylabel('y (m)')
title('Projectile Motion')
show()

