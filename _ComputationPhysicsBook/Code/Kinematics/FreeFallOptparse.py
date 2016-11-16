#!/usr/bin/env python
# Program Falling Ball
"""
This program uses the Euler method to solve for the motion of a ball
dropped from rest close to the surface of Earth. The program depends
on the function VelocityLinearDrag to execute the Euler method.
"""
import sys, EulerFreeFall
import numpy as np
import matplotlib.pyplot as plt
#from optparse import OptionParser
import optparse
import optparse_gui
t = 0.0	# initialize time to 0.0
g = 9.8	# define acceleration due to gravity
#
usage = "usage: %prog [options] args"
if 1 == len( sys.argv ):
    option_parser_class = optparse_gui.OptionParser
else:
    option_parser_class = optparse.OptionParser
        
parser = option_parser_class( usage = usage, version='0.1' )
parser.add_option("-f", "--file", dest="filename", default = 'junk.dat',
    help="filename for output")
parser.add_option('-v', '--v_initial', dest='v', type='float',
    help='initial velocity', default=0.0)
parser.add_option('-t', '--v_terminal', dest='vterminal', type='float',
    help='terminal velocity', default=20.0)
parser.add_option('-m', '--tmax', dest='tmax', type='float',
    help='maximum simulation time', default=5.0)
parser.add_option("-a", "--dt", dest="dt",\
    help="time steps", action="append", default='0.01')
    
option, args = parser.parse_args()

print 'args: %s' % args
print 'options: %s' % option

#define the variables we need
filename = option.filename
v = option.v   # sets initial velocity
vinitial = v	   # save initial velocity for later use
vterminal = option.vterminal
tmax = option.tmax
timeSteps = option.dt  # saves dt values as a string list called timeSteps
print filename, v, vterminal, tmax, timeSteps
#
# Main Loop:
for n in timeSteps:
    dt = float(n)  # convert string into a floating point number.
    fname = filename + str(n) + '.dat'
    outfile = open(fname, 'w')  # open file for writing
# Write Header line as first row in data file
    outfile.write('time (s) \t speed \n')
    outfile.write('%g \t %g \n' % (t,v))
# Main calculation loop
imax = int(tmax/dt)
for i in range(imax+1):
	t=i*dt
	v = EulerFreeFall.VelocityLinearDrag(v, dt, 9.8, vterminal)
	outfile.write('%g \t %g\n' % (t,v))
		
outfile.close()
data = np.load(fname, skiprows=1) #(numpy function)
xaxis = data[ : , 0 ]		# first column
yaxis = data[ : , 1 ]		# second column
plt.plot( xaxis, yaxis, marker='.', markersize=7, linestyle='None')
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
plt.legend(legendstring.split(', '), loc='best') # writes legend
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.title('Vertically Dropped Ball')
plt.show()

