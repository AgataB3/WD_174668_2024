import math


def zad1():
    print("Wyrażenie 1: ", round(((math.e ** 4) - math.log(34, 2)) ** (1 / 3), 2))
    print("Wyrażenie 2: ", round((math.log(20) + math.cos(45) + math.e) ** (1 / 3), 2))
    print("Wyrażenie 3: ", round((math.log(20, 3) + math.sin(45) * 5 / 8) ** (1 / 4), 2))
    print("Wyrażenie 4: ", round(math.log(23, 3) + (math.sin(34) + 5) ** (1 / 3), 2))
    print("Wyrażenie 5: ", round((math.log2(32) + math.pi + math.sin(56)) ** (1 / 4), 2))


def zad2():
    n = int(input("Podaj wysokosc wiezy, nie wieksza niz 10: "))
    if n > 10:
        print("Za wysoka wieza.")
    else:
        for i in range(n):
            print("A" * (i + 1))


def zad3():
    n = int(input("Podaj wysokosc piramidy, nie wieksza niz 10: "))
    if n > 10:
        print("Za wysoka piramida.")
    else:
        for i in range(n):
            print(" " * (n - i), "A" * (i * 2 + 1))


def main():
    # zad1()
    # zad2()
    zad3()


main()
