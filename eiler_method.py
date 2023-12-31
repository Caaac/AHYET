import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + f(y[i-1]) * (t[i] - t[i-1])
    return y

def f(y):
    return y

t = np.linspace(0, 2, 100)
y0 = 1
y = euler_method(f, y0, t)

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler method solution for y\'=y and y(0)=1')
plt.show()