# File Euler2D.py
"""
This file defines functions needed to implement the Euler method for 
one dimensional free fall with air resistance.  
B is the value for B/m for the particle in question (passed to this routine
from the calling program.)
"""
import numpy as np
g=9.8
def newVelocity(vx, vy, dt, B):
    vx = vx - B*np.sqrt(vx**2 + vy**2)*vx*dt
    vy = vy - B*np.sqrt(vx**2 + vy**2)*vy*dt - g*dt
    return vy,vy

def newPosition(x, y, vx, vy,dt):
    x = x + vx*dt
    y = y + vy*dt
    return x,y