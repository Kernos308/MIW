import numpy as np


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