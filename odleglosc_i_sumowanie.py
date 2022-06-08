import numpy as np
import random
import math


plik = open("australian.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e: float(e), line.replace('\n', '').split(' '))))

x = [1, 1, 1, 1, 1, 8, 5, 6, 3, 2, 1, 1, 1, 1]

def od(x, lista):
    wyn = []
    for j in range(len(lista)):
        tmp = 0
        for e in range(len(lista[j]) - 1):
            tmp += (lista[j][e] - x[e]) ** 2
        tmp = tmp ** (1 / 2)
        wyn.append((lista[j][-1], tmp))
    return wyn


listaod = od(x, lista)
print(listaod)


def grupowanie(lista):
    tmp = {}
    for i in range(len(lista)):
        c = lista[i][0]
        if c not in tmp:
            tmp[c] = []
        tmp[c].append(lista[i][1])
    return tmp


grup = grupowanie(listaod)
print(grup)


def sumowanie(grupa, k):
    wyn = {}
    for j in range(len(grupa)):
        tmp = sorted(grupa[j])
        sumka = 0
        for i in range(k):
            sumka += tmp[i]
        c = list(grupa)[j]
        if c not in wyn:
            wyn[c] = 0
        if sumka in wyn.values():
            return "Brak odpowiedzi"
        wyn[c] += sumka

    index = min(wyn, key=wyn.get)
    return (index, wyn[index])


wyn = sumowanie(grup, 5)
print(wyn)