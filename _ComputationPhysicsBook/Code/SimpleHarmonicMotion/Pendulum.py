##!/usr/bin/env python
# Program Pendulum
"""
This program uses the Euler method to solve for the motion of a simple
pendulum. 
"""
import sys, pendSolve,getInputs
from pylab import *
import numpy
from math import *

#	READ IN RUN PARAMETERS (new method; optparse) 
#	and Define variables needed; contained in getInputs.py
filename, omega, theta, t, tmax, timeSteps, g, l= getInputs.getInputs()
omega_initial = omega	#save initial velocity for later use
theta_initial = theta 

# Main Loop: 
for n in timeSteps:
	dt=float(n) # need to convert string into a floating point number.
	fname=filename+str(n)+'.dat'
	outfile=open(fname, 'w')	# open file for writing			
	# Write Header line as first row in data file
	kinetic, potential, totalE = pendSolve.energy(theta,omega,g,l)
	outfile.write('time (s) \t theta (rad) \t omega (rad/s) \t kinetic \t potential \t totalEnergy (J) \n')	
	outfile.write('%g \t %g \t %g \t %g \t %g \t %g \n' % (t,theta, omega, kinetic, potential, totalE))
	# Main calculation loop
	imax = int(tmax/dt)
	for i in range(imax+1):
		t=i*dt
		state=complex(theta,omega)
#		state=pendSolve.eulerCromer(state,dt,g,l)
		state=pendSolve.RK4(state,dt,g,l)
		omega = state.imag
		theta = state.real
		kinetic, potential, totalE = pendSolve.energy(theta,omega,g,l)
		outfile.write('%g \t %g \t %g \t %g \t %g \t %g \n' % (t,theta, omega, kinetic, potential, totalE))
#		outfile.write('%g \t %g \t %g \t %g \n' % (t,theta, omega, totalE))
		
	outfile.close()
	data = numpy.loadtxt(fname, skiprows=1)	# (pylab function)
	tAxis = data[ : , 0 ]			# first column
	thetaAxis = data[ : , 1 ]			# second column
	omegaAxis = data[ : ,2]
	keAxis = data[ : ,3]
	peAxis = data[ : , 4]
	eAxis = data[ : , 5]
	subplot(211)
	plot( omegaAxis, thetaAxis, marker='.', markersize=2, linestyle='None')
	subplot(212)
	plot( tAxis, thetaAxis, marker='.', markersize=2, linestyle='None')
	t=0.0
	i=0
	omega=omega_initial
	theta=theta_initial

# set up plot parameters and plot data
legendstr=[]	#the following four lines set up the legend 
for j in range(len(timeSteps)):
	legendstr.append('dt=' + timeSteps[j])
legendstring=str(legendstr[:])
legendstring=legendstring.strip("[ ]")
print legendstring
legend(legendstring.split(', '), loc='best') # writes legend
xlabel('theta')
ylabel('omega')
title('Simple Pendulum')
axis([-pi, pi, -1*max(omegaAxis), max(omegaAxis)])

show()

