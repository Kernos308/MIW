import numpy as np
import random
import math


plik = open("australian.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e: float(e), line.replace('\n', '').split(' '))))


print(lista)

def euk(a, b):
    tmp = 0
    for e in range(len(lista[a])):
        tmp += (lista[a][e] - lista[b][e]) ** 2
    tmp = tmp ** (1 / 2)
    return tmp



def euk2(lista1, lista2):
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    a = v2 - v1
    c = math.sqrt(np.dot(a, a))
    return c


print("------euklides----")
euklides = euk(0, 1)
print(euklides)
euklides2 = euk2(lista[0], lista[1])
print(euklides2)