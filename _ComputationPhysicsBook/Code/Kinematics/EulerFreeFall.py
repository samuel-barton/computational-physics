# File EulerFreeFall.py
"""
This file defines functions needed to implement the Euler method for 
one dimensional free fall with air resistance.  
"""
def VelocityLinearDrag(v,dt,g=9.8, vt=30.0):
	return (v + g*(1-v/vt)*dt)
		
def PositionLinearDrag(x, v, dt):
	return (x + v*dt)

def newVelocityNoDrag(v, dt=0.01, g=9.8):
	return ( v - g*dt)
	
def newPositionNoDrag(y, v, dt):
	return (y + v*dt)	
