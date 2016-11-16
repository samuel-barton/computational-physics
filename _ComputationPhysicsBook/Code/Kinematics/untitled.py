#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Paul Nakroshis on 2011-10-16.
Copyright (c) 2011 Dept. of Physics, Univ. of Southern Maine. All rights reserved.
"""

from pylab import *
from verticalMotion import *

y=100.0
v=0.0
t=0.0
dt=0.001
times=[]
yPos=[]
yVel=[]

while y>0.0:
	times.append(t)
	yPos.append(y)
	yVel.append(v)
	y=PositionQD(y, v, dt)
	v=YVelocityQD(abs(v), v, dt, g=9.8, vt=30.0)
	t=t+dt
	
plot(times,yPos)
show()