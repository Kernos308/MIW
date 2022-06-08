import numpy as np

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