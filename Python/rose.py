from pylab import *
t=linspace(0, 16*pi, 600)
amplitude=100
n=7
d=8
k=n/d
x=amplitude*cos(k*t)*tan(t)
y=amplitude*sin(k*t)*tan(t)
plot(x,y)
show()
