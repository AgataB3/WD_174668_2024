import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl


def zad1():
    xlsx = pd.ExcelFile('datasets/imiona.xlsx')
    df = pd.DataFrame(pd.read_excel(xlsx, header=0))

    grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
    print(grupa)
    grupa.plot(xlabel='Rok', ylabel='Liczba', rot=0,
               legend=False, title='Liczba dzieci urodzonych w danym roku')
    plt.xticks(rotation=45)
    plt.xticks(np.arange(df["Rok"], 2018, step=1))
    plt.show()


def zad2():
    xlsx = pd.ExcelFile('datasets/imiona.xlsx')
    df = pd.DataFrame(pd.read_excel(xlsx, header=0))

    grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
    print(grupa)

    grupa.plot(kind='bar', xlabel='Płeć', ylabel='Ilość w milionach', rot=0,
               legend=False, title='Liczba urodzonych chlopcow i dziewczynek')
    plt.show()


def main():
    # zad1()
    zad2()


main()
