import numpy as np

def zad1():
    y = np.arange(3, 46, 3)
    print(y)


def zad2():
    b = np.array([3.4, 5.6, 7.7, 8.8])
    print(b)
    a = np.array(b, dtype='int64')
    print(a)


def zad3(n):
    x = np.arange(n)



def main():
    # zad1()

    # zad2()

    #zad 3
    n = int(input("Wprowadz n: "))
    print(zad3(n))


main()