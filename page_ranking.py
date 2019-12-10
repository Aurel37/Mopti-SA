import numpy as np
from generation_matrice import gen_matrix, w

def page_ranking(A, m,  X):
    val_propres, vect_propres = np.linalg.eig(A)
    n = len(A)
    edges = []
    val_sorted = []
    for i in range(n):
        val_sorted.append((abs(val_propres[i]), vect_propres[i]))
    #print(val_sorted)
    val_sorted = sorted(val_sorted, key=lambda colonnes: colonnes[0])
    vect_principal = val_sorted[0][1]
    vect_sorted = []
    for i in range(n):
        vect_sorted.append((abs(vect_principal[i]), i))
    vect_sorted = sorted(vect_sorted, key=lambda colonnes: colonnes[0])
    #print(vect_sorted)
    for i in range(n-1, n-m-1, -1):
        edges.append(vect_sorted[i])
    print(edges)
    for i in edges:
        X[i] = True
        for j in range(n):
            A[i][j] = 0
            A[j][i] = 0

m = gen_matrix(5, w)
print(m)
page_ranking(m, 2)


