from math import *
def omega(theta, omega, dt, g=9.8, l=1.0):
	return (omega -(g/l)*sin(theta)*dt)

def theta(theta, omega, dt, g=9.8, l=1.0):
		return (theta + omega*dt)
		
def euler(state, dt, g=9.8, l=1.0):
	omega_i=state.imag
	theta_i=state.real
	omega = omega_i -(g/l)*sin(theta_i)*dt
	theta = theta_i + omega_i*dt
	state=complex(theta,omega)
	return (state)
	
def eulerCromer(state, dt, g=9.8, l=1.0):
	omega_i=state.imag
	theta_i=state.real
	omega = omega_i -(g/l)*sin(theta_i)*dt
	theta = theta_i + omega*dt
	state=complex(theta,omega)
	return (state)

def energy(theta, omega, g=9.8, l=1.0):
	kinetic = 0.5*l*l*omega*omega
	potential = g*l*(1.0-cos(theta))
	totalE = kinetic + potential
	return kinetic, potential, totalE
	
		
def RK4(state,dt, g=9.8,l=1.0):
	omega=state.imag
	theta=state.real
	def deriv_v(theta,omega,dt,g=9.8,l=1.0):
		return (-(g/l)*sin(theta)*dt)
	if theta > 15*pi/180.0:
		dt=dt/100.
		for n in range(100):
			k1v = deriv_v(theta,omega,dt,g,l)
			k1x = omega*dt
			k2v = deriv_v(theta+k1x/2.0,omega+k1v/2.0,dt,g,l)
			k2x = (omega+k1v/2.0)*dt
			k3v = deriv_v(theta+k2x/2.0,omega+k2v/2.0,dt,g,l)
			k3x = (omega+k2v/2.0)*dt
			k4v = deriv_v(theta+k3x,omega+k3v,dt,g,l)
			k4x = (omega+k3v)*dt
			omega = omega + (k1v+2*k2v+2*k3v+k4v)/6.0
			theta = theta + (k1x+2*k2x+2*k3x+k4x)/6.0
		dt=dt*100
		state=complex(theta,omega)
		return (state)
	else:
		k1v = deriv_v(theta,omega,dt,g,l)
		k1x = omega*dt
		k2v = deriv_v(theta+k1x/2.0,omega+k1v/2.0,dt,g,l)
		k2x = (omega+k1v/2.0)*dt
		k3v = deriv_v(theta+k2x/2.0,omega+k2v/2.0,dt,g,l)
		k3x = (omega+k2v/2.0)*dt
		k4v = deriv_v(theta+k3x,omega+k3v,dt,g,l)
		k4x = (omega+k3v)*dt
		omega = omega + (k1v+2*k2v+2*k3v+k4v)/6.0
		theta = theta + (k1x+2*k2x+2*k3x+k4x)/6.0
		state=complex(theta,omega)
		return (state)
	