import math
import random


def zad1():
    wynik = 0
    for x in range(30,61):
        wynik += (math.e**(math.sin(x))+math.log(32, 3))**(1/4)
    print(round(wynik, 2))


def zad2(min, max, ile):
    if ile>0:
        try:
            lista = []
            roznica = []
            for i in range(ile):
                lista.append(random.randrange(min, max+1))
            print(lista)
            for i in range(ile):
                tmp = []
                for j in range(0, ile):
                    if lista[i] == lista[j]:
                        continue
                    else:
                        tmp.append(lista[i]-lista[j])
                roznica.append(tmp)
            return roznica
        except ValueError:
            return "Max musi byc wieksze od min."
    else:
        return "Ilosc elementow musi byc wieksza od 0."




def main():
    print("Zadanie 1: ")
    zad1()

    print("Zadanie 2: ")
    min = int(input("Element minimalny listy: "))
    max = int(input("Element maksymalny listy: "))
    ile = int(input("Ile elementow wygenerowac: "))
    print(zad2(min, max, ile))


main()