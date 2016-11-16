#
# This script calculates the area under the curve y=x**2 from x=0 to x=1, using
# inscribed rectangles.
#

def f(x):
    return ( x**2 )

i, areaLower, areaUpper, areaTrapezoid = 0, 0.0, 0.0, 0.0   # initialize variables
nRectangles=1000

xmin, xmax = 0.0, 1.0
dx = (xmax - xmin)/nRectangles
x=xmin

while i<nRectangles:
    x = xmin + i*dx
    areaLower = areaLower + f(x)*dx
    areaUpper = areaUpper + f(x+dx)*dx
    areaTrapezoid = areaTrapezoid + f(x)*dx + 0.5*dx*(f(x+dx)-f(x))
    i = i + 1
print "the lower limit of the area is = ", areaLower
print "the upper limit of the area is = ", areaUpper
print "the average is = ", (areaLower+areaUpper)/2.0
print "the trapezoidal approximation is = ", areaTrapezoid
