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
                if W(list_proba[i], list_proba[j])<list_proba[i]:
                    res[i][j] = 1
                    res[j][i] = 1
    return res

def transition(matrix, X, p_heal, p_infect):
    """
    matrix is an array that represents a graph
    X is a list of bool that informs if the edge i is sick

    The function realize one transition of the graph 
    """
    n = len(matrix)
    for i in range(n):
        if (X[i] and uniform(0,1)<p_heal): # proba de s'auto soigner
            X[i] = False
        else:
            count_voisin = 0 # nombre de voisin malade 
            poids = 0 # poids des voisins malade 
            for j in range(n):
                if (matrix[i][j] > 0 and X[j]): # si on est connecté à qlqn de malade 
                    count_voisin += 1
                    poids += matrix[i][j]
            if (count_voisin >0 and uniform(0,1)<(p_infect*poids)/count_voisin):
                        X[i] = True
def w(x,y):
    return (x+y)/2
