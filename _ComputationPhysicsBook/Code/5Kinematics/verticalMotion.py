def linearDragEuler(v,dt,g=9.8, vt=2.0):
	return (v + g*(1-v/vt)*dt)
		
def VelocityEulerLinearDrag(v,dt,g=9.8, vt=30.0):
	return (v + g*(1-v/vt)*dt)

def PositionEulerLinearDrag(y, v, dt):
	return (y + v*dt)
##
##	Functions for Quadratic Drag (QD) are below; the position function will
##	update either x or y
##
def XVelocityQD(v, vx, dt, g=9.8, vt=30.0):
	return (vx - (g*v*vx*dt)/(vt*vt) )

def PositionQD(pos, vel, dt):
	pos = pos + vel*dt
	if pos<0:
		pos=0
	return (pos)
	
def YVelocityQD(v, vy, dt, g=9.8, vt=30.0):
	return (vy -g*dt - (g*v*vy*dt)/(vt*vt) )
	