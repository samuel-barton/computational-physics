#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Paul Nakroshis on 2011-10-20.
Copyright (c) 2011 Department of Physics, USM. All rights reserved.
"""

from pylab import *

def newOmega(theta, omega, dt,  g=9.8, l=1.0):
	return (omega - g*theta*dt/l)

def newTheta(theta, omega, dt):
		