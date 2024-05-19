import numpy as np


def zad1():
    y = np.arange(3, 46, 3)
    print(y)


def zad2():
    b = np.array([3.4, 5.6, 7.7, 8.8])
    print(b)
    a = b.astype('int64')
    print(a)


def zad3(n):
    y = np.arange(1, n*n+1)
    y = y.reshape((n, n))
    return y


def zad4(podstawa, ilosc):
    x = np.logspace(1,
                    ilosc,
                    num=ilosc,
                    base=podstawa,
                    dtype='int')
    return x


def zad5(x):
    y = np.arange(x-1, -1, -1)
    d = np.diag(y)
    return d


def zad6():
    x = np.array([['O', 'N', 'K', 'O', 'J', 'F'],
                  ['W', 'L', 'O', 'D', 'B', 'P'],
                  ['P', 'B', 'N', 'D', 'I', 'A'],
                  ['A', 'I', 'I', 'D', 'T', 'R'],
                  ['M', 'B', 'E', 'D', 'E', 'B'],
                  ['G', 'X', 'C', 'C', 'E', 'D'],
                  ])
    return x


def zad7(n):
    y = np.zeros((n, n), dtype='int')
    zm = 0
    zm2 = n
    for i in range(n):
        for x in range(1, n+1):
            if x-1+zm < n:
                y[i][x-1+zm] = 2*x
        zm += 1
        for x in range(1, n+1):
            if n-x-zm2 > -1:
                y[i][n-x-zm2] = 2*(x+1)
        zm2 -= 1
    return y


def main():
    print("zad1:")
    zad1()

    print("\nzad2:")
    zad2()

    print("\nzad3:")
    n = 5
    print(zad3(n))

    print("\nzad4:")
    podstawa = 2
    ilosc = 4
    print(zad4(podstawa, ilosc))

    print("\nzad5:")
    x = 5
    print(zad5(x))

    print("\nzad6:")
    print(zad6())

    print("\nzad7:")
    n = 6
    print(zad7(n))


main()
