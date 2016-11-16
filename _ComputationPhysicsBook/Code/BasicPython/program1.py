#!/usr/bin/env python
import sys
from math import *

try:
	v0 = float(sys.argv[1]) # initial velocity
	t = float(sys.argv[2])	# time			
except:
	print "Usage:", sys.argv[0], "v0 time"
	sys.exit(1)

y = v0*t-4.9*t**2	#  position 
print "ball's position is", y, "meters at t=", t, "seconds"