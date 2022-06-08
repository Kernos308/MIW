import numpy as np
import random
import math


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