import sys
from math import *
from optparse import OptionParser
def getInputs():
	t=0.0		# initialize time to 0.0
	g=9.8		# define acceleration due to gravity
	l=1.0		# define length of pendulum
	parser = OptionParser()
	# define all options:
	parser.add_option('-f', '--filename', dest='filename', type='string', help='filename for output', default='pendy')
	parser.add_option('-v', '--v_initial', dest='omega', type='float',
	help='initial velocity', default=0.0)
	parser.add_option('-a', '--theta', dest='theta', type='float',
	help='initial angle in degrees (measured from vertical)', default=15.0)
	parser.add_option('-m', '--tmax', dest='tmax', type='float',
	help='maximum simulation time', default=10.0)
	parser.add_option('-t', '--dt', dest='dt',
	help='time steps', action = 'append')	# the append action makes a list.
	#now read from command line
	option, args = parser.parse_args(sys.argv[1: ])
	#define the variables we need
	filename=option.filename
	omega=(option.omega)/l 	# sets initial angular velocity (omega =v/l)
	theta=option.theta * pi/180. # convert input angle to radians
	tmax = option.tmax
	timeSteps=option.dt	# saves dt values as a string list called timeSteps
	print filename, omega, theta, tmax, timeSteps
	print 'total e =', 0.5*l*l*omega*omega + g*l*(1.0-cos(theta))
	return  filename, omega, theta, t, tmax, timeSteps, g, l
	