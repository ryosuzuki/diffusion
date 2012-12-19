from pylab import *
from scipy.integrate import quad
import numpy as np
import matplotlib.mlab as mlab

c = 0.1
beta = 0.1
lammda = 0.4

def f(m, q):
	n = 1
	if - n / q < m and m < n / q:
		return q / (2.0 * n)
	else:
		return 0
	
def F(m, q):
	if m < 0 or q == 0:
		return 0
	else:
		f_prime = lambda x: f(x, q)
		y, error = quad(f_prime, -100, m)
		print "F ( ) = " + str(y)
		return y

for i in range(21):
  m = 0.05 * i
  for j in range(21):
    q = 0.05 * j
    delta_m = lammda * (F(m, q) - m)
    delta_q = c * m - beta * q
    arrow(m, q, delta_m / 10, delta_q / 10, width=0.003)

n = 1000

m = 0
q = 0.01
mass_0 = []
quality_0 = []

for _ in xrange(n):
  mass_0.append(m)
  quality_0.append(q)
  m = m + lammda * (F(m, q) - m)
  q = q + c * m - beta * q

m = 0
q = 0.22
mass_1 = []
quality_1 = []

for _ in xrange(n):
  mass_1.append(m)
  quality_1.append(q)
  m = m + lammda * (F(m, q) - m)
  q = q + c * m - beta * q


plot(mass_0, quality_0, linewidth=2)
plot(mass_1, quality_1, linewidth=2)
axis([0, 1.0, 0, 1.0])
xlabel("Mass ($m_t$)", fontname='serif')
ylabel("Quality ($q_t$)", fontname='serif')
legend(["(0, 0.2)", "(0, 0.22)"], "lower right")
show()
