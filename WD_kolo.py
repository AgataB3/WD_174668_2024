import math
import random


def zad1():
    wynik = 0
    for n in range(14,33):
        wynik += (n**(math.e)+math.cos(n))**(1/5)
    print(round(wynik, 2))


def zad2(min, max, ile):
    if ile>0:
        try:
            lista = []
            for i in range(ile):
                lista.append(random.randrange(min, max+1))
            print(lista)
            for i in range(ile):
                lista[i] = lista[i]*(-1)
            return lista
        except ValueError:
            return "Max musi byc wieksze od min."
    else:
        return "Ilosc elementow musi byc wieksza od 0."


def zad3(nazwa_pliku):
    p = open(nazwa_pliku)
    for i in p:
        s = {}
        max = 0
        lista = []
        for m in i:
            if m.isdigit():
                lista.append(m)
        for j in lista:
            if j in s:
                s[j] += 1
            else:
                s[j] = 1
        for k in s:
            if (s[k] > max):
                max = s[k]
        licznik = 0
        for l in s:
            if s[l] == max:
                licznik += 1
                x = l
        if licznik == 1:
            print(x)
        else:
            print(lista[random.randint(0, len(lista)-1)])
    p.close()


def zad4(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return "Taki trojkat nie istnieje."
    else:
        if(a**2+b**2 == c**2):
            return a*b/2
        else:
            return "To nie trojkat prostokatny"


def main():
    print("Zadanie 1: ")
    zad1()

    print("Zadanie 2: ")
    min = int(input("Element minimalny listy: "))
    max = int(input("Element maksymalny listy: "))
    ile = int(input("Ile elementow wygenerowac: "))
    print(zad2(min, max, ile))

    print("Zadanie 3: ")
    zad3("liczby.txt")

    print("Zadanie 4: ")
    a = int(input("Wprowadz pierwsza przyprostokatna: "))
    b = int(input("Wprowadz druga przyprostokatna: "))
    c = int(input("Wprowadz przeciwprostokatna: "))
    print(zad4(a, b, c))


main()