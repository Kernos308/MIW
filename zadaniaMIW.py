import numpy as np
import random
import math


plik = open("australian.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e: float(e), line.replace('\n', '').split(' '))))


# print(lista)

def euk(a, b):
    tmp = 0
    for e in range(len(lista[a])):
        tmp += (lista[a][e] - lista[b][e]) ** 2
    tmp = tmp ** (1 / 2)
    return tmp


pd = {0: [], 1: []}
n = len(lista[0])
for i in range(1, len(lista)):
    if lista[i][n - 1] == 0:
        pd[0].append(euk(0, i))
    if lista[i][n - 1] == 1:
        pd[1].append(euk(0, i))

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

# n = random.randint(10,100)
def wieksze(a, b):
    if a>b:
        return a
    else:
        return b

def funkcja(x):
    return x

def losowanie(x, y):
    return x + random.random()/(random.random()+1) * (y-x)

def czyNadY(x, y):
    if (y>0 and y<=funkcja(x)):
        return 1
    elif (y<0 and y<=funkcja(x)):
        return -1
    return 0

def MonteCarlo(startX, koniecX, n):
    punkty = 0
    startY = 0
    koniecY = math.ceil(wieksze(funkcja(startX), funkcja(koniecX)))
    for i in range(n):
        punkty += czyNadY(losowanie(startX, koniecX), losowanie(startY, koniecY))
    wynik = (punkty/n) * ((koniecX - startX) * (koniecY - startY))
    return wynik

print("------MonteCarlo-----")
print(MonteCarlo(0, 1, 100))


def prostokat(start, koniec, n):
    dx = (koniec - start) / n
    wyn = 0
    function = 'i'
    for i in range(n):
        i = i * dx + start
        fx1 = eval(function)
        i += dx
        fx2 = eval(function)
        wyn += 0.5 * dx * (fx1 + fx2)
    return wyn

print("------prostokat-----")
print(prostokat(0, 1, 100))

def trapez(start, koniec, n):
    function = 'i'
    dx = (koniec - start) / n
    wyn = 0
    for i in range(n):
        i = i * dx + start
        fx1 = eval(function)
        i += dx
        fx2 = eval(function)
        wyn += 0.5 * dx * (fx1 + fx2)
    return wyn


print("------trapez-----")
print(trapez(0, 1, 100))

nowa = lista

# for i in range(len(nowa)):
#     nowa[i] = nowa[i][:-1]

#print("------nowa------")
#print(nowa)



def kolorowanie(lista):
    # for i in range(len(lista)):
    #     wyb = random.randint(0, 100)
    #     if wyb % 2 == 0:
    #         lista[i].append(1.0)
    #     else:
    #         lista[i].append(0.0)
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



# regresja:wzór x*beta=y macierz x jedna koluma to 1 a druga to obserwacje(pkt x), y to wektor od y1 do yn
# dla bety = B0 + B1X1 = y1               y = ax+b
# B1 to odchylenie, a B0 podnosi jeśli jest na plus a obniża na minus
# punkty do obliczenia (2,1) (5,2) (7,3) (8,3)
# powinno wyjść 2/7(B0) i 5/14(B1)


x = np.array([2, 5, 7, 8])
y = np.array([1, 2, 3, 3])

def regresja(x, y):
    jedynki = np.ones(len(x))
    X = np.column_stack((jedynki,x))
    nawias = np.dot(X.T, X)
    potega = np.linalg.inv(nawias)
    a = np.dot(potega, X.T)
    B = np.dot(a, y)
    return B



jedynki = np.ones(len(x))
a = np.column_stack((jedynki,x))
print(pow(np.dot(a.T,a), -1))
print('-----regresja--------')
print(regresja(x, y))





def e(u):
    suma = 0
    for i in range(len(u)):
        suma+=u[i]**2
    dlugoscU = suma**(1/2)
    return u/dlugoscU

def projekcja(u,v):
    licznik = np.dot(v.T,u)
    mianownik = np.dot(u.T,u)
    wynik = licznik/mianownik * u
    return wynik

def rozkładQR(A, wymiar):
    V = A.T
    for i in range(wymiar):
        if i ==0:
            v1 = V[:,i]
            u1 = v1
            e1 = e(u1)
        elif i==1:
            v2 = V[:,i]
            u = v2 - projekcja(u1, v2)
            ei = e(u)
            Q = np.vstack([e1, ei])
        else:
            v = A[i, :]
            suma=0
            for k in range(i):
                suma+=(projekcja(u1, v))
            u = v - suma
            ei = e(u)
            Q = np.vstack([Q, ei])
    R = np.dot(Q, V)
    return R

macA = np.array(([1,1,0],[0,1,1]))

print('-----rozkładQR--------')
print(rozkładQR(macA,2))



# def zlozMacierz(v1,v2):
#     a = np.column_stack(v1,v2)
#     return a
# def rozkładQR(v1,v2):
#     A = zlozMacierz(v1, v2)
#     u1 = v1
#     e1 = e(u1)
#     u2 = v2 - projekcja(u1, v2)
#     e2 = e(u2)
#     Q = macierzA(e1,e2)
#     R = np.dot(Q.T, A)
#     return R

# def wartosciWlasne(macierzA):
#     wymiary = macierzA.shape
#     rozmiar = wymiary[0]
#     macierzJednostkowa = np.eye(rozmiar)
#     wektorZerowy = np.zeros((rozmiar,1))
#     l = Symbol('l')
#     macierz = macierzA - (l*macierzJednostkowa)
#
#
#     return
# print('-----linalg.eig--------')
# print(np.linalg.eig(macA))
# print('-----wartosci wlasne--------')
# print(wartosciWlasne(macA))




# normalizacja macierzy

BT = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, -1, -1, -1, -1],
              [1, 1, -1, -1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, -1, -1],
              [1, -1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, -1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, -1, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, -1]])


def mnozenie(macierzB):
    wynik = np.dot(macierzB,macierzB.T)
    return wynik

# print(mnozenie(BT))
wektorXA = [8, 6, 2, 3, 4, 6, 6, 5] #transponowane
def normMac(macierzB):
    macierzNorm = np.array([macierzB[0,:]/math.sqrt(np.dot(macierzB[0,:],macierzB[0,:]))])
    wymiary = macierzB.shape
    for i in range(1,wymiary[0]):
        norm = macierzB[i,:]/math.sqrt(np.dot(macierzB[i,:],macierzB[i,:]))
        macierzNorm = np.append(macierzNorm,[norm],axis=0)
    return macierzNorm
print("---------normalizacja i mnożenie---------")
print(np.dot(normMac(BT), wektorXA))

macierzDoSVD = np.array(([1,2,0], [2,0,2]))
def bazaV(macierzA):
    mnozenie = np.dot(macierzA.T, macierzA)
    w, v = np.linalg.eig(mnozenie)
    return w, v
def bazaU(macierzA):
    mnozenie = np.dot(macierzA, macierzA.T)
    w, v = np.linalg.eig(mnozenie)
    return w, v

def SVD(macierzA):
    V = bazaV(macierzA)
    U = bazaU(macierzA)
    wymiary = macierzA.shape
    if (wymiary[0]>wymiary[1]):
        singularne = np.sqrt(V[0])
        singularne = sorted(singularne, reverse=1)
        s = np.diag(singularne)
        macierzS = s
    if (wymiary[1]>wymiary[0]):
        singularne = np.sqrt(U[0])
        singularne = sorted(singularne, reverse=1)
        s = np.diag(singularne)
        zero = np.array([[0],[0]])
        macierzS = np.append(s, zero, axis=1)
    return U[1], macierzS, V[1].T

print("-----------SVD-----------")
print(SVD(macierzDoSVD))

