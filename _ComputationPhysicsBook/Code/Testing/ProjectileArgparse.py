#!/usr/bin/env python
# Program Projectile
"""
This program uses the Euler method to solve for the motion of a 
sphere launched from the ground with initial speed v at angle theta above
the horizontal. The program simulates the motion of 
a) a sphere with zero air resistance
b) a stainless steel sphere (radius 1cm, density 8 g/cm^3) 
c) a balsa wood sphere (radius 1cm, density 0.16 g/cm^3)
The program uses quadratic drag and assumes that Fd = -B*v^2, so that
B/m = \frac{3}{16}\frac{\rho_air}{\rho_sphere} \frac{1}{R}
"""
import sys, Euler2D
from pylab import *
import argparse 
t=0.0		# initialize time to 0.0
g=9.8		# define acceleration due to gravity
xinitial=0.0
yinitial = 0.0 
# define B/m for zero drag, Stainless Steel, and Balsa Wood spheres
# of radius 1.0 cm:
BoverM = [0.0, 3*1.2/(16*8000.*0.01), 3*1.2/(16*160*0.01)] 
#
#	READ IN RUN PARAMETERS 
#	and Define variables needed   
parser = argparse.ArgumentParser()

# define all options:
parser.add_argument('--filename', dest='filename', \
action="store", help='output filename', default="junk.dat")

parser.add_argument('--v_initial', dest='v', type=float, \
default=0.0, help='initial velocity')

parser.add_argument('--theta', dest='theta', type=float, \
default = 30.0, help='launch angle in degrees')

parser.add_argument('--dt', dest='dt', help='time steps', \
action='append')	# the append action makes a list. 

#now read from command line 
input = parser.parse_args()
#define the variables we need 
filename=input.filename
# set initial velocity:
v=input.v 	
#save initial velocity for later use (for multiple runs):
vinitial = v 
# set initial angle, and convert to radians:
theta = input.theta 
theta_R = theta*pi/180.
# saves dt values as a string list called timeSteps:
timeSteps = input.dt
print filename, v, theta, timeSteps
vx = v*cos(theta_R)
vy = v*sin(theta_R)

#
# Main Loop: 
for n in timeSteps:
	dt=float(n)# need to convert string into a floating point.
	fname=filename+str(n)+'.dat'
	outfile=open(fname, 'w')	# open file for writing			
	# Write Header line as first row in data file
	outfile.write('time (s) \t xpos \t ypos \t xvel \t yvel \t speed \n')	
        outfile.write('%g \t %g \t %g \t %g \t %g \t %g \t %g \n' % \
                      (t,xinitial,yinitial, vx, vy, sqrt(vx**2 + vy**2))
	# Main calculation loop
	imax = int(tmax/dt)
	for i in range(imax+1):
		t=i*dt
		v = EulerFreeFall.VelocityLinearDrag(v, dt, 9.8, vterminal)
		outfile.write('%g \t %g\n' % (t,v))
		
	outfile.close()
	data = loadtxt(fname, skiprows=1)	# (pylab function)
	xaxis = data[ : , 0 ]			# first column
	yaxis = data[ : , 1 ]			# second column
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
xlabel('time (s)')
ylabel('velocity (m/s)')
title('Vertically Dropped Ball')
show()

