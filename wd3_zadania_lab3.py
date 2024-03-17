import random
import math


def zad1():
    A = [1 - x for x in range(1, 11)]
    print(A)
    B = [4 ** i for i in range(8)]
    print(B)
    C = [x for x in B if x % 2 == 0]
    print(C)


def zad2():
    listy1 = []
    for i in range(10):
        listy1.append(random.randrange(0, 100))
    print(listy1)
    listy2 = [y for y in listy1 if y % 2 == 0]
    print(listy2)


def zad3():
    p = {'Awokado': "sztuki",
         'Orzechy włoskie': "kg",
         'Banany': "kg",
         'Pomidory w puszce': "sztuki"}
    lista = [x for x in p.keys() if p[x] == "sztuki"]
    print(lista)


def zad4():
    a = int(input("Podaj pierwszy bok trojkata: "))
    b = int(input("Podaj drugi bok trojkata: "))
    c = int(input("Podaj trzeci bok trojkata: "))
    if (a**2 == b**2 + c**2) | (b**2 == a**2 + c**2) | (c**2 == a**2 + b**2):
        print("Trojkat jest prostokatny.")
    else:
        print("Trojkat nie jest prostokatny.")


def pole_trapezu(a=10, b=5, h=5):
    return 1/2 * (a+b) * h


def zad5():
    a = int(input("Podaj dlugosc pierwszej podstawy: "))
    b = int(input("Podaj dlugosc drugiej podstawy: "))
    h = int(input("Podaj dlugosc wysokosci: "))
    print(f'Pole trapezu: {pole_trapezu(a, b, h)}')


def ciag(a1=1, b=4, ile=10):
    iloczyn = 1
    for i in range(ile):
        iloczyn *= a1
        a1 *= b
    return iloczyn


def zad6():
    a1 = int(input("Podaj wartosc poczatkowa: "))
    b = int(input("Podaj wielkosc o ile mnozone sa kolejne elementy: "))
    ile = int(input("Podaj ile elementow mnozyc: "))
    print(ciag(a1, b, ile))


def zad7():
    x = int(input("Podaj liczbe: "))
    try:
        print(math.sqrt(x))
    except ValueError:
        print("Nie mozna pierwiastkowac ujemnej liczby.")


def main():
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    # zad5()
    # zad6()
    zad7()


main()
