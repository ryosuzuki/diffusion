from pylab import *

m = 0.20
q = 0.06

beta = 0.1
delta = 0.1

x1 = []
y1 = []


n = 60
for _ in xrange(n):
#while (1-m)*q - delta*m > 0.0000000000000001:
#    if m < 10 and q < 10:
        print m
        print q
        x1.append(m) 
        y1.append(q)
        m = m + ((1-m) * m * q - delta * m)
        q = q + ((1-q) * q * m - beta * q)


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


figure()


lines = plot(x1, y1, 'k')
setp(lines, color='r', linewidth=2.0)

hoge = 0.3

x2 = arange(0, hoge, 0.01)
y2 = delta / gamma_1 * x2**(1-alpha)

plot(x2, y2)

y3 = arange(0, hoge, 0.01)
x3 = beta / gamma_2 * y3**(1-alpha)
#y3 = gamma_2 / beta * x3**(1/(1-alpha))

plot(x3, y3)

show()
