import numpy as np
import math

print("\nZad1: ")
a = np.array([3, 6, 9])
b = np.array([1, 4, 8])
print(a)
print(b)
print(a * b)

print("\nZad2: ")
a = np.array([[3, 6, 9],
              [4, 7, 9],
              [2, 1, 7]])
b = np.array([[3, 4, 8],
              [4, 6, 9],
              [8, 8, 8]])
print(f'Macierz a:\n{a}')
print(f'Macierz b:\n{b}')
print(f'Wartosci minimalne dla kolumn macierzy a: {a.min(axis=0)}')
print(f'Wartosci minimalne dla kolumn macierzy b: {b.min(axis=0)}')
print(f'Wartosci minimalne dla wierszy macierzy a: {a.min(axis=1)}')
print(f'Wartosci minimalne dla wierszy macierzy b: {b.min(axis=1)}')

print("\nZad3: ")
c = a.dot(b)
print(c)

print("\nZad4: ")
a = np.array([[1, 2, 7],
               [7, 3, 9],
               [6, 2, 8]])
print(a)
print(a.dtype)
b = np.array([[5.7, 2, math.pi],
               [9.1, 2.8, 8],
               [math.e, 2.9, 8.3]])
print(b)
print(b.dtype)
c = a * b
print(c)
print(c.dtype)

print("\nZad5: ")
a = np.array([[math.pi/2, 5, 1],
              [3*math.pi/2, 4, 0]])
b = np.sin(a)
print(b)

print("\nZad6: ")
a = np.array([[4, math.pi, 1],
              [0, 2, 2*math.pi]])
b = np.cos(a)
print(b)

print("\nZad8: ")
a = np.arange(9).reshape((3, 3))
print(a)
for x in a:
    print(x)

print("\nZad9: ")
a = np.arange(9).reshape((3, 3))
for x in a.flat:
    print(x)

print("\nZad10: ")
a = np.arange(81).reshape((9, 9))
print(a)
a = a.reshape((3, 27)) #dzielniki liczby 81
print(a)

print("\nZad11: ")
a = np.arange(12)
print(a)
a = a.reshape((3, 4))
print(a)
b = a.reshape((4, 3))
print(b)
c = a.reshape((2, 6))
print(c)
a = a.ravel()
b = b.ravel()
c = c.ravel()
print(a)
print(b)
print(c)
