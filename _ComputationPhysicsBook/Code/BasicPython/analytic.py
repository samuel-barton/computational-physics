def height(v0,t,g=9.8):
	if t==0 and v0<0.0: 
		print "initial velocity must be >= 0"
		sys.exit(1)
	elif (v0*t-0.5*g*t**2) >=0.0: 
		return v0*t-0.5*g*t**2
	else:
		print "ball has hit the ground"
		return 0.0