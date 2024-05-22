import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 4, 100)
plt.subplot(1, 3, 1)
plt.plot(x, x**2+5, label="x^2+5")
plt.xlim(-3, 3)
plt.ylim(4, 14)
plt.xlabel("x")
plt.ylabel("Wartosci funkcji")
plt.legend(loc='upper center')
plt.title("Wykres funkcji f(x)=x^2+5")
plt.subplot(1, 3, 3)
plt.plot(x, x**2+5, linestyle='none', color='red', marker='o', markersize=4)
plt.plot(x, -x**2+4*x, linestyle='none', color='green', marker='o', markersize=4)
plt.xlim(-3, 3)
plt.ylim(-20, 15)
plt.legend(labels=['x^2+5', '-x^2+4x'], loc='lower center')
plt.title("Wykres dwoch funkcji")
plt.xlabel("x")
plt.ylabel("Wartosci funkcji")
plt.savefig('Agata_Bronk_zad2.png')
plt.show()
