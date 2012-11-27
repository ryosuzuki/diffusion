from pylab import *

m = 0.3
q = 0.0001

c = 1
beta = 0.7
delta = 0.3

gamma_q = 0.8
gamma_m = 0.5
alpha = 1

x1 = []
y1 = []


n = 40
for _ in xrange(n):
#while (1-m)*q - delta*m > 0.0000000000000001:
    print m
    print q
    x1.append(m) 
    y1.append(q)
    m = m + alpha*gamma_m*(1-m)*q - delta * m
    q = q + gamma_q*(1-q)*m - beta*q

print x1
print y1

t = []
i = 0

for _ in xrange(n):
    t.append(i)
    i = i+1

plot(t, x1)
plot(t, y1)
show()


lines = plot(x1, y1, 'k')
setp(lines, color='r', linewidth=2.0)

show()
