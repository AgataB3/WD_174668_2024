import random


def zad1():
    A = [1-x for x in range(1, 11)]
    print(A)
    B = [4**i for i in range(8)]
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
    produkty = {"Awokado": "sztuki",
                "Orzechy włoskie": "kg",
                "Banany": "kg",
                "Pomidory w puszce": "sztuki"}

    
def main():
    # zad1()
    # zad2()
    zad3()


main()