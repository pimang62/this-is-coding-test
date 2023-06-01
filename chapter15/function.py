import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 10)
y = np.linspace(0, 100, 10)

def f(x):
    y = -(x-10)**2
    return y

plt.plot(x, f(x))
plt.show()