from random import uniform
import numpy as np

def gen_matrice(n,w):
    res = np.zeros((n,n))
    liste_proba = [uniform(0,1) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i>j:
                print(w(liste_proba[i], liste_proba[j]))
                print(liste_proba[i])
                if w(liste_proba[i], liste_proba[j])<liste_proba[i]:
                    res[i][j] = 1
                    res[j][i] = 1
    return res

