# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def mans_atan(x, n):
    k = 0
    a = 1
    S = a
    Rfirst = x/np.sqrt(1+x**2)
    while k < n:
        k = k + 1
        Rtop = x**2*(2*k-1)*((2*k)*(2*k-1))
        Rdown = 4*(2*k+1)*(1+x**2)*(k**2)
        R = Rtop/Rdown
        a = a * R
        S = S + a
    return Rfirst*S

x = np.arange (0.0,4.0,0.01)
y = np.arctan(x)

plt.plot(x,y)

for i in range(1,5,1):
     f = mans_atan(x,i)
     plt.plot(x,f)

plt.show ()


