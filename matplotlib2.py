import matplotlib.pyplot as plt
import numpy as np


def zad1():
    x = np.linspace(1, 20, 20)
    plt.plot(x, 1/x, label="f(x) = 1/x")
    plt.axis([1, len(x), 0, 1])
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()


def zad2():
    x = np.linspace(1, 19, 20)
    plt.plot(x, 1/x, ':>', c='green', label="f(x) = 1/x")
    plt.axis([0, len(x), 0, 1])
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()


def zad3():
    x = np.arange(0, 30, 0.1)
    sin = np.sin(x)
    cos = np.cos(x)
    plt.plot(x, sin, color='g', label="sin(x)")
    plt.plot(x, cos, color='b', label="cos(x)")
    plt.legend(loc='upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def main():
    # zad1()
    # zad2()
    zad3()


main()