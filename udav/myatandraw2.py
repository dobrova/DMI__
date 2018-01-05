# -*- coding: utf-8 -*-
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def mans_atan(x):
    k = 0
    a = 1
    S = a
    Rfirst = x/np.sqrt(1+x**2)
    while k < 500:
        k = k + 1
        Rtop = x**2*(2*k-1)*((2*k)*(2*k-1))
        Rdown = 4*(2*k+1)*(1+x**2)*(k**2)
        R = Rtop/Rdown
        a = a * R
        S = S + a
    return Rfirst*S

N=10000
a=0.0
b=3.0
c=-0.5
d=1.5
x = []
y = []

plt.plot(x,y)

for i in range(N):
    x.append(random.uniform(a,b))
for i in range(N):
    y.append(random.uniform(c,d))

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < mans_atan(x[i]) and y[i] > 0) \
    or (y[i] > mans_atan(x[i]) and y[i] < 0):
        green_x.append(x[i])
        green_y.append(y[i])
    else:
        red_x.append(x[i])
        red_y.append(y[i])

plt.plot(green_x,green_y,'go')
plt.plot(red_x,red_y,'rv')
plt.grid()



plt.show()


areaRect = (b-a)*(d-c)
print areaRect
areaFunc = areaRect * len(green_x) / N
print areaFunc
