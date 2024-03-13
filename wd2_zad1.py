import math


def a():
    AB = float(input("Podaj dlugosc odcinka AB: "))
    AC = float(input("Podaj dlugosc odcinka AC: "))
    BC = float(input("Podaj dlugosc odcinka BC: "))
    kat_ACB = AC**2/2*AC*BC + BC**2/2*AC*BC - (AB**2/2*AC*BC)
    print(math.cos(kat_ACB))


def b():
    AC = float(input("Podaj dlugosc odcinka AC: "))
    BC = float(input("Podaj dlugosc odcinka BC: "))
    kat_ACB = float(input("Podaj wartosc kata: "))
    AB = AC**2 + BC**2 - 2*AC*BC*math.cos(kat_ACB)
    print(math.sqrt(AB))


def main():
    # a()
    b()


main()
