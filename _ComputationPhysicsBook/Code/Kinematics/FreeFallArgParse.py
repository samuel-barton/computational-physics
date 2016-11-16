#!/usr/bin/env python
# Program Falling Ball
"""
This program uses the Euler method to solve for the motion of a 
ball dropped from rest close to the surface of Earth. The 
program depends on the function VelocityLinearDrag to execute 
the Euler method. 
"""
import sys, EulerFreeFall
import numpy as np
import matplotlib.pyplot as plt
import argparse 
import datetime
t=0.0		# initialize time to 0.0
g=9.8		# define acceleration due to gravity
#
######	READ IN RUN PARAMETERS        ###################
######	and Define variables needed   ###################

parser = argparse.ArgumentParser()

# define all options:
parser.add_argument('--filename', dest='filename', \
action="store", help='output filename', default="junk.dat")

parser.add_argument('--v_initial', dest='v', type=float, \
default=0.0, help='initial velocity')

parser.add_argument('--v_terminal', dest='vterminal', type=float, \
default=2.0, help='terminal velocity')

parser.add_argument('--tmax', dest='tmax', type=float, \
default=0.2, help='maximum simulation time')

parser.add_argument('--dt', dest='dt', help='time steps', \
action='append')	# the append action makes a list. 

parser.add_argument("--savePlot", dest='savePlot', action="store",\
default='none', help='Save a hardcopy of plot? (specify .pdf or png)' )

#now read from command line 
input = parser.parse_args()
# define the variables we need 
filename=input.filename
# set initial velocity:
v=input.v 	
#save initial velocity for later use (for multiple runs):
vinitial = v 
vterminal = input.vterminal
tmax = input.tmax
savePlot = input.savePlot
# saves dt values as a string list called timeSteps:
timeSteps = input.dt
print "output File = ",filename
print "intitial V = ", v
print "terminal V = ", vterminal
print "tmax = ", tmax
print "timeSteps = ", timeSteps
print "savePlot = ", savePlot
##
#####
#####################################################
#####

# Main Loop: 
for n in timeSteps:
	dt=float(n)# need to convert string into a floating point.
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
	data = np.loadtxt(fname, skiprows=1)  # (numpy function)
	xaxis = data[ : , 0 ]		# first column
	yaxis = data[ : , 1 ]		# second column
	plt.plot( xaxis, yaxis, marker='.', markersize=7, linestyle='None')
	t=0.0
	i=0
	v=vinitial

# set up plot parameters and plot data

legendstr=[]	#the following four lines set up the legend 
for timestep in timeSteps:
	legendstr.append('dt = ' + timestep)
legendstring=str(legendstr[:])
legendstring=legendstring.strip("[ ]") + ', Analytic Solution'
#print legendstring
plt.legend(legendstring.split(', '), loc='best') # writes legend
plt.xlabel('time (s)', fontsize = 18)
plt.ylabel('velocity (m/s)', fontsize = 18)
plt.title('Vertically Dropped Ball', fontsize = 18)
plt.ylim(0, .21)
# if user specified a hardcopy of the file, then save a uniquely named
# copy as either a pdf of png. Then display plot to screen (in all cases). 
if savePlot == 'pdf':
    now = datetime.datetime.now()
    fname = str(now.year) + str(now.month) + str(now.day) + "-" +\
      str(now.hour) + str(now.minute) + str(now.second) + ".pdf"
    plt.savefig(fname, dpi=600)
elif savePlot == 'png':
    now = datetime.datetime.now()
    fname = str(now.year) + str(now.month) + str(now.day) + "-" +\
      str(now.hour) + str(now.minute) + str(now.second) + ".png"
    plt.savefig(fname, dpi=600)
elif savePlot == 'none':
    pass

# create array for plot of analytic function for comparison:
a = np.arange(0,tmax,dt)
c = vterminal*(1-np.exp(-g*a/vterminal))
plt.plot(a,c,'k--')
plt.show()

