""""
 This script calculates the area under the curve y=x**2 from x=0 to x=1, using 
 a Monte Carlo Method.
""""


from random import *
from pylab import *
def f(x):
	return x**2

nThrows = 1000000
nHits = 0
x, y = zeros(nThrows), zeros(nThrows)
x, y = 
for i in range(nThrows):
	x = uniform(0,1)
	y = uniform(0,1)
	if y<=f(x): 
		nHits = nHits + 1
print "Area estimate after %g throws is = %g" % (nThrows, 1.0*nHits/nThrows)