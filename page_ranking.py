import numpy as np



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
    res = 0
    n = len(u)
    for i in range(n):
        res += u[i]**2
    return res**(1/2)


def somme_colonne_i(A, i):
    res = 0
    n = len(A)
    for k in range(n):
        res += A[k, i]
    return res


def normalisation(A):
    n = len(A)
    RES = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            somme = somme_colonne_i(A, j)
            if somme != 0:
                RES[i, j] = A[i, j]/somme
    return RES


def page_ranking(Weight_mat, m, X, seuil):
    n = len(A)
    u0 = [1 for i in range(n)]
    u1 = [0 for i in range(n)]
    Weight_mat_n = normalisation(Weight_mat)
    while (norme(soustraction(u0, u1)) > seuil):
        u1 = copie_vect(u0)
        print(Weight_mat_n)
        u0 = np.dot(Weight_mat_n, u0)
        print('inside', u0)
        u0 = u0/norme(u0)
    indice = []
    propre_indice = []
    print("u0_end", u0)
    for i in range(n):
        propre_indice.append((abs(u0[i]), i))
    propre_indice = sorted(propre_indice, key=lambda colonnes: colonnes[0])
    for i in range(n-1, n-m-1, -1):
        indice = propre_indice[i][1]
        X[indice] = True
        for j in range(n):
            A[indice][j] = 0
            A[j][indice] = 0

