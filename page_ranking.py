import numpy as np
from generation_matrice import gen_matrix, w


def soustraction(u0, u1):
    n = len(u0)
    res = []
    for i in range(n):
        res.append(u0[i] - u1[i])
    return res


def copie_vect(u):
    res = []
    for i in u:
        res.append(i)
    return res


def norme(u):
    test = 0
    res = 0
    n = len(u)
    for i in range(n):
        res += u[i]**2
    return res**(1/2)

def somme_ligne_i(A,i):
    res = 0
    n = len(A)
    for k in range(n):
        res += A[i,k]
    return res

def normalisation(A):
    n = len(A)
    RES = np.zeros((n,n))
    for i in range(n):
        somme = somme_ligne_i(A,i)
        for j in range(n):
            if (somme != 0):
                RES[i,j] = A[i,j]/somme
    return RES

def page_ranking(A, m, X, seuil):
    n = len(A)
    u0 = [1 for i in range(n)]
    u1 = [0 for i in range(n)]
    B = normalisation(A)
    while (norme(soustraction(u0, u1)) > seuil):
        u1 = copie_vect(u0)
        u0 = np.dot(B, u0)
        print('inside', u0)
        u0 = u0/norme(u0)
    indice = []
    propre_indice = []
    print("u0_end", u0)
    for i in range(n):
        propre_indice.append((abs(u0[i]), i))
    propre_indice = sorted(propre_indice, key = lambda colonnes: colonnes[0])
    for i in range(m):
        indice = propre_indice[i][1]
        X[indice] = True
        for j in range(n):
            A[indice][j] = 0
            A[i][indice] = 0

A = gen_matrix(5, w)
X = [True, False, True, False, False]
print(A)
page_ranking(A, 2, X, 0.01)
print(A)


