import pandas as pd
import numpy as np
import openpyxl

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.DataFrame(pd.read_excel(xlsx, header=0))

# zad 1
# print("Liczba nadanych imion > 1000:")
# print(df[df['Liczba']>1000])
# print("\nRekordy z imieniem 'Agata':")
# print(df[df['Imie']=='AGATA'])
print("\nSuma wszystkich urodzonych dzieci: ")
print(df.agg({'Liczba':['sum']}))
print("\nSuma wszystkich urodzonych dzieci między 2000-2005: ")
print(df[(df['Rok']>=2000) & (df['Rok']<=2005)].agg({'Liczba':['sum']}))
print("\nSuma wszystkich urodzonych chłopców i dziewczynek: ")
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))



