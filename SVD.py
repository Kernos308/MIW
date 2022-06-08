import numpy as np

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