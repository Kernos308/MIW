import math
import numpy as np

plik = open("australian.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e: float(e), line.replace('\n', '').split(' '))))

def srednia(vektor):
    n = len(vektor)
    ones = np.ones(n)
    suma = np.dot(vektor, ones)
    sr = suma / n
    return sr


wynik1 = srednia(lista[0])
print("------srednia------")
print(wynik1)

def wariancja(vektor):
    n = len(vektor)
    sr_vektor = srednia(vektor)
    a = vektor - sr_vektor
    wr = np.dot(a, a) / n
    return wr

print("------wariancja------")
wektor5 = np.ones(10)
wektor5 = wektor5 *5
print(wariancja(lista[0]))

def odchylenie_standardowe(vektor):
    w = wariancja(vektor)
    wyn = w**(1/2)
    return wyn

print("------odchylenie standardowe------")
print(odchylenie_standardowe(lista[0]))