"""
 This script calculates the area under the curve f(x), where f(x) is assumed to
 have a maximum value of 1 and a minimum value of 0 on the interval 0 to 1
"""

from random import *
from functions import *


def monteCarloDarts(n, f):
    nHits = 0
    for i in range(n):
        x = uniform(0,1)
        y = uniform(0,1)
        if y <= f(x):
            nHits = nHits + 1

    return (1.0*nHits/n)
