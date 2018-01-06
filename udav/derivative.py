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

a = 0
b = 3 * np.pi
x = np.arange(a,b,0.05)
y = mans_atan(x)

plt.plot(x,y)
plt.grid()

n = len(x)
y_prim = []
for i in range(n-1):
    delta_y = y[i+1] - y[i]
    delta_x = x[i+1] - x[i]
    y_prim.append(delta_y / delta_x)

n = len(x)
y_2prim = []
for i in range(n-2):
    delta_y_prim = y_prim[i+1] - y_prim[i]
    delta_x = x[i+1] - x[i]
    y_2prim.append(delta_y_prim / delta_x)


plt.plot(x[:n-1],y_prim)
plt.plot(x[:n-2],y_2prim)
plt.show()
