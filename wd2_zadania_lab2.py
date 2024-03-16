import sys


def zad1():
    x = 0
    z = input("Wprowadz zdanie: ")
    for i in range(len(z)):
        if z[i] == " ":
            x += 1
    print(f'Ilosc slow: {x + 1}')


def zad2():
    sys.stdout.write('Wczytaj liczbe: ')
    a = sys.stdin.readline()
    sys.stdout.write('Wczytaj liczbe: ')
    b = sys.stdin.readline()
    sys.stdout.write('Wczytaj liczbe: ')
    c = sys.stdin.readline()
    a = int(a)
    b = int(b)
    c = int(c)
    print(f'Wynik: {a ** b + c}')


def zad3():
    n = input("Wprowadz napis: ")
    if n == n[::-1]:
        print("Napis jest palindromem.")
    else:
        print("Napis nie jest palindromem.")


def zad4():
    y = True
    x = int(input("Wprowadz liczbe: "))
    for i in range(2, x):
        if x % i == 0:
            print(f'{x} nie jest liczba pierwsza.')
            y = False
            break
    if y:
        print(f'{x} jest liczba pierwsza.')


def zad5():
    x = 0
    for i in range(1, 1001):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if s == i:
            x += 1
    print(f'Ilosc liczb dokoskonalych do liczby 1000 to: {x}')


def zad6():
    n = int(input("Wprowadz ilosc liczb: "))
    lista = []
    for i in range(n):
        t = input("Jaki typ liczby chcesz wprowadzi? 'i' dla int, 'f' dla float: ")
        if t == 'i':
            lista.append(int(input("Wprowadz liczbe: "))**2)
        elif t == 'f':
            lista.append(float(input("Wprowadz liczbe: "))**2)
    print(lista)


def zad7():
    lista = []
    i = 0
    while i < 10:
        i += 1
        x = int(input("Wprowadz liczbe: "))
        if x % 2 == 0:
            lista.append(x)
    print(lista)


def zad8():
    lista = []
    s = {}
    n = int(input("Podaj ilosc elementow: "))
    for i in range(n):
        lista.append(input("Wprowadz element: "))
    for i in range(n):
        if lista[i] in s:
            s[lista[i]] += 1
        else:
            s[lista[i]] = 1
    print(s)
    for i in range(n):
        if not lista[i].isdigit():
            del s[lista[i]]
    print(s)




def main():
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    # zad5()
    # zad6()
    # zad7()
    # zad8()

main()
