import numpy as np
import math
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

print(mnozenie(BT))
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