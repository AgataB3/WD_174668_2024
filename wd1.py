import math
import random


def zad1():
    x = input("Wczytaj liczbe: ")
    lista = []
    while x:
        if x == 'end':
            print(lista)
            break
        elif x.isdigit():
            lista.append(x)
            print(lista)
            x = input("Wczytaj liczbe: ")
        else:
            print(lista)
            x = input("Wczytaj liczbe: ")


def zad2():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    if a > 0:
        print("Funkcja jest rosnaca")
    elif a < 0:
        print("Funkcja jest malejaca")
    else:
        print("Funkcja jest stala")


def zad3():
    a1 = int(input("Podaj a1: "))
    b1 = int(input("Podaj b1: "))
    a2 = int(input("Podaj a2: "))
    b2 = int(input("Podaj b2: "))
    if a1 == a2:
        print("Proste sa rownolegle")
    elif a1 * a2 == -1:
        print("Proste sa prostopadle")
    else:
        print("proste nie sa ani rownolegle ani prostopadle")


def dlugosc_odcinka(x1=0, y1=0, x2=0, y2=0):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def zad4():
    x1 = int(input("Podaj wspolrzedna x1: "))
    y1 = int(input("Podaj wspolrzedna y1: "))
    x2 = int(input("Podaj wspolrzedna x2: "))
    y2 = int(input("Podaj wspolrzedna y2: "))
    x3 = int(input("Podaj wspolrzedna x3: "))
    y3 = int(input("Podaj wspolrzedna y3: "))
    a = dlugosc_odcinka(x1, y1, x2, y2)
    b = dlugosc_odcinka(x1, y1, x3, y3)
    c = dlugosc_odcinka(x3, y3, x2, y2)
    if a ** 2 + b ** 2 == c ** 2:
        print(f'Dlugosc przeciwprostokatnej:{c}')
    elif a ** 2 + c ** 2 == b ** 2:
        print(f'Dlugosc przeciwprostokatnej:{b}')
    elif c ** 2 + b ** 2 == a ** 2:
        print(f'Dlugosc przeciwprostokatnej:{a}')
    else:
        print(f'To nie trojkat prostokatny')


def zad4_wersja2():
    a = int(input("Podaj 1 bok: "))
    b = int(input("Podaj 2 bok: "))
    c = math.sqrt(a ** 2 + b ** 2)
    print(f'Dlugosc przeciwprostokatnej: {c}')


def suma_ciagu(a1=1, r=1, ile=10):
    suma = 0
    element = a1
    for i in range(ile):
        suma += element
        element += r
    return suma


def zad5():
    a1 = int(input("Wartosc poczatkowa: "))
    r = int(input("Wielkosc o ile rosna kolejne elementy: "))
    ile = int(input("Ile elementow sumowac: "))
    print(f'Suma ciagu: {suma_ciagu(a1, r, ile)}')


def dodaj_znak(lista):
    for i in range(len(lista)):
        lista[i] += "!"
    return lista


def dodaj_znak2(lista):
    lista2 = lista
    for i in range(len(lista2)):
        lista2[i] += "!"
    return lista2


def zad6():
    lista = []
    n = int(input("Ile chcesz dodac napisow? "))
    for i in range(n):
        lista.append(input("Wprowadz napis: "))
    # print(dodaj_znak(lista))
    print(dodaj_znak2(lista))


def guess_the_number():
    punkty = 0
    for i in range(5, 0, -1):
        y = random.randrange(1, 11)
        x = int(input(f'Zgadnij liczbę: {i}\n'))
        if x == y:
            print(f'Wylosowana liczba to {y}. Zdobywasz 10 punktów.')
            punkty += 10
        else:
            print(f'Wylosowana liczba to {y}. Tracisz punkt.')
            punkty -= 1
    print(f'Koniec gry. Twoja punktacja to: {punkty} pkt')


def zad7():
    guess_the_number()


def zad8():
    s = int(input("Wprowadz liczbe: "))
    y = s
    while s >= 10:
        x = s
        s = 0
        while x > 0:
            r = x % 10
            s += r
            x //= 10
    print(f'Digital root liczby {y} to: {s}')


def multipli_game():
    p = 0
    b = 0
    for i in range(1, 11):
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
        odp = int(input(f'Pytanie {i}: {x} x {y} = '))
        if odp == x*y:
            print('Poprawna odpowiedz!')
            p += 1
        else:
            print(f'Bledna odpowiedz, poprawna odpowiedzia jest {x*y}.')
            b += 1
    print(f'Koniec gry!\nBledne odpowiedzi: {b}\nPoprawne odpowiedzi: {p}')


def zad9():
    multipli_game()


def main():
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    # zad4_wersja2()
    # zad5()
    # zad6()
    # zad7()
    # zad8()
    zad9()


main()