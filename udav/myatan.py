# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def mans_atan(x):
    k = 0
    a = 1
    S = a
    Rfirst = x/math.sqrt(1+x**2)

    while k < 500:
        k = k + 1
	Rtop = x**2*(2*k-1)*((2*k)*(2*k-1))
	Rdown = 4*(2*k+1)*(1+x**2)*(k**2)
        R = Rtop/Rdown
        a = a * R
        S = S + a
    return Rfirst*S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))

print mans_atan(x)
print math.atan(x)
