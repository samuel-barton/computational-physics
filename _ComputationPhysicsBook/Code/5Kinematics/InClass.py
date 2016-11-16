from pylab import *
from EulerFreeFall import *
v = 9.8 # initial velocity
y = 100.0 # initial position
t=0.0
dt = 0.1
timeValues=[]
position=[]
velocity=[]
timeValues.append(t)
position.append(y)
velocity.append(v)
while y > 0:
	y = newPositionNoDrag(y,v,dt)
	v = newVelocityNoDrag(v, dt, 9.8)
	t = t + dt
	timeValues.append(t)
	position.append(y)
	velocity.append(v)
plot(timeValues,position)
show()
