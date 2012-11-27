from pylab import *

m = 0.25
q = 0.75

c = 1
beta = 0.5
delta = 0.05

x1 = []
y1 = []


n = 1000
for _ in xrange(n):
#while (1-m)*q - delta*m > 0.0000000000000001:
#while m <5:
    print m
    print q
    x1.append(m) 
    y1.append(q)
    m = m + (1-m) * m * q - delta * m
    q = q + (1-q) * q * m - beta * q

print x1
print y1
lines = plot(x1, y1, 'k')
setp(lines, color='r', linewidth=2.0)


x2 = arange(0, 0.9, 0.01)
y2 = delta / (1-x2)

plot(x2, y2)

y3 = arange(0, 0.9, 0.01)
x3 = beta / (1-y3)

plot(x3, y3)


show()
