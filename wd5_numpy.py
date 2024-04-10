import numpy as np

print("Zad1:")
a = np.array([3, 6, 9])
b = np.array([1, 4, 8])
print(a)
print(b)
print(a*b)

print("\nZad2:")
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

print("\nZad3:")
