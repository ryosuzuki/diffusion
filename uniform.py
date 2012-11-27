from pylab import *
from scipy.integrate import quad
import numpy as np
import matplotlib.mlab as mlab

m = 0
q = 0.0001

c = 1
beta = 0.1
lammda = 0.4

n = 30
t = 0

def f(m, q):
	mean = 0.1 / q
	variance = 0.2
	sigma = sqrt(variance)
	if m < -1 / q or m > 1 / q:
		return 0
	else:
		return q / 2.0
	
def F(m, q):
	if m < 0:
		return 0
	else:
		f_prime = lambda x: f(x, q)
		y, error = quad(f_prime, -10, m)
		print "F ( ) = " + str(y)
		return y

time = []
mass = []
quality = [] 
for _ in xrange(n):
	print "--------"
	print "t = " + str(t)  
	print "m = " + str(m)
	print "q = " + str(q)
	time.append(t)
	mass.append(m) 
	quality.append(q)
	t = t + 1
	m = m + lammda * (F(m, q) - m)
	q = q + c * m - beta * q

	
print time
print mass
print quality
subplot(1,2,1)
lines = plot(time, mass, 'k')
setp(lines, color='r', linewidth=2.0)

subplot(1,2,2)
lines = plot(time, quality, 'k')
setp(lines, color='r', linewidth=2.0)
show()
