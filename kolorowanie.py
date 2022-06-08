import numpy as np
import random
import math


plik = open("australian.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e: float(e), line.replace('\n', '').split(' '))))


nowa = lista

def euk2(lista1, lista2):
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    a = v2 - v1
    c = math.sqrt(np.dot(a, a))
    return c

def kolorowanie(lista):
    return [punkt[:14] + [float(random.randint(0, 1))] for punkt in lista]

kolorowanie(nowa)


def wyznaczanie_srodkow(lista):
    min_odleglosci = {}
    odleglosci = {}
    for klasa in range(2):
        for i in range(len(lista)):
            distance = 0
            if lista[i][-1] == klasa:
                for j in range(len(lista)):
                    if lista[j][-1] == klasa:
                        distance += euk2(lista[i], lista[j])
                odleglosci[i] = distance
        min = list(dict(sorted(odleglosci.items(), key=lambda value: value[1])).keys())[0]
        min_odleglosci[klasa] = min
        odleglosci = {}
    return min_odleglosci


def nowe_srodki(lista):
    kolorowanie(lista)
    nowa_lista = lista

    licznik_zmian = 0
    licznik = 0

    while True:
        licznik += 1
        min_odleglosci = wyznaczanie_srodkow(nowa_lista)

        for klasa in range(2):
            for i in range(len(nowa_lista)):

                if i in min_odleglosci.values():
                    continue

                if nowa_lista[i][-1] == klasa:
                    aktualna_odl = euk2(nowa_lista[min_odleglosci.get(klasa)],
                                              nowa_lista[i])
                    odl_do_zera = euk2(nowa_lista[min_odleglosci.get(0)],
                                           nowa_lista[i])
                    odl_do_jedynki = euk2(nowa_lista[min_odleglosci.get(1)],
                                          nowa_lista[i])
                    if aktualna_odl > odl_do_jedynki:
                        nowa_lista[i][-1] = float(1)
                        licznik_zmian += 1
                    if aktualna_odl > odl_do_zera:
                        nowa_lista[i][-1] = float(0)
                        licznik_zmian += 1

        ilosc_zer = 0
        ilosc_jedynek = 0

        for element in nowa_lista:
            if element[14] == 1.0:
                ilosc_jedynek += 1
            if element[14] == 0.0:
                ilosc_zer += 1

        print(f'ilosc zer: {ilosc_zer} | ilosc jedynek:{ilosc_jedynek}')
        if licznik_zmian == 0:
            break
        licznik_zmian = 0

    return nowa_lista

print("----kolorowanie-----")
nowe_srodki(nowa)