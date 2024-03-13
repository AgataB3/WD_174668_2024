import random


def przegrany(win, pick):
    j = True
    while j:
        x = random.randrange(1, 5)
        if x != win and x != pick:
            j = False
    return x


def zmiana(x, pick):
    k = True
    while k:
        y = random.randrange(1, 5)
        if y != x and y != pick:
            k = False
    return y


def zmiana_bramki():
    wygrane = 0
    for i in range(10000):
        win = random.randrange(1, 5)
        pick = random.randrange(1, 5)
        x = przegrany(win, pick)
        y = zmiana(x, pick)
        if y == win:
            wygrane += 1
    print(f'Procent wygranych gier w przypadku zmiany bramki: {wygrane / 10000 * 100}%')


def pierwotny_wybor():
    wygrane = 0
    for i in range(10000):
        win = random.randrange(1, 5)
        pick = random.randrange(1, 5)
        if pick == win:
            wygrane += 1
    print(f'Procent wygranych gier w przypadku pozostania przy pierwotnym wyborze: {wygrane / 10000 * 100}%')


def main():
    zmiana_bramki()
    pierwotny_wybor()


main()
