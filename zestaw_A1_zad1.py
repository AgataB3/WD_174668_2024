import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10)
plt.plot(x, (x**2+4)/(2**x), label="f(x) = (x^2+4)/2^x")
plt.xlabel("x")
plt.ylabel("Wartosci funkcji")
plt.legend()
plt.title("Wykres funkcji")
plt.show()
