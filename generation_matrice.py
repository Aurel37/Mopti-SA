from random import uniform
import numpy as np

def gen_matrix(n,W):
    """
    n in an integer that represent the number of edges of the graph
    """
    res = np.zeros((n,n))
    list_proba = [uniform(0,1) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i>j:
                if W(liste_proba[i], liste_proba[j])<liste_proba[i]:
                    res[i][j] = 1
                    res[j][i] = 1
    return res

def transition(matrix, X, p_heal, p_infect, p_sick):
    """
    matrix is an array that represents a graph
    X is a list of bool that informs if the edge i is sick

    The function realize one transition of the graph 
    """
    n = len(matrix)
    for i in range(n):
        if (X[i] and uniform(0,1)<p_heal):
            X[i] = False
        elif (uniform(0,1)<p_sick):
            X[i] = True
        else:
            for j in range(n):
                if (matrix[i][j] and X[i]):
                    if (uniform(0,1)<p_infect):
                        X[j] = True
def w(x,y):
    return (x+y)/2

G = gen_matrice(5,w)

X = [True, False, False, True, True]

transition(G, X, 0.5, 0.3, 0.7)

print(X)
