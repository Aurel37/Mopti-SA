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


def page_ranking(Link_mat, people_vac, X_vac, seuil):
    """
    DESCRIPTION

    Perform the PageRanking algorithm on the adjacency matrix Link_mat, return 
    the new adjacency matrix

    VARIABLES

    Link_mat : a square matrix representing a graph
    people_vac : number of people to remove from the graph
    X_vac : a vector of True, if the edge i is removed from the graph, 
    the vertex i turns to False
    seuil : a float mesure
    """
    n = len(Link_mat)
    u0 = [1 for i in range(n)]
    u1 = [0 for i in range(n)]
    Link_mat_n = normalisation(Link_mat)
    while (norme(soustraction(u0, u1)) > seuil):
        u1 = copie_vect(u0)
        u0 = np.dot(Link_mat_n, u0)
        if norme(u0) != 0:
            u0 = u0/norme(u0)
    indice = []
    propre_indice = []
    for i in range(n):
        propre_indice.append((abs(u0[i]), i))
    propre_indice = sorted(propre_indice, key=lambda colonnes: colonnes[0])
    for i in range(n-1, n-people_vac-1, -1):
        indice = propre_indice[i][1]
        X_vac[indice] = False
        for j in range(n):
            Link_mat[indice][j] = 0
            Link_mat[j][indice] = 0
