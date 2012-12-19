from pylab import *
from scipy.integrate import quad
import numpy as np
import matplotlib.mlab as mlab


def f(m, q):
	if q == 0:
		q = 0.00001
	mean = 1 / q
	variance = 1
	sigma = sqrt(variance)
	return mlab.normpdf(m, mean, sigma)
	
def F(m, q):
	if m < 0:
		return 0
	else:
		f_prime = lambda x: f(x, q)
		y, error = quad(f_prime, -100, m)
		return y

mass = []
quality = [] 
m=0
while m < 0.9:
	q = 10.0
	min_d = 1000
	while q > 0:
		delta = F(m, q) - m
		if delta < 0:
			break
		if delta < min_d:
			min_s = sign
			min_d = delta
			min_q = q
		q = q - 0.1
	print "min = " + str(min_d)
	print "m = " + str(m)
	print "q = " + str(min_q)
	mass.append(m) 
	quality.append(min_q)
	m =  m + 0.01

print mass
print quality
lines = plot(mass, quality, 'k')
setp(lines, color='r', linewidth=2.0)
show()
