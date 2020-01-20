from random import uniform, shuffle
import numpy as np
#False : heal, True : sick


def gen_vect(n_pop, p_sick):
    X = []
    for i in range(n_pop):
        if (uniform(0,1)<p_sick):
            X.append(True)
        else:
            X.append(False)
    return X


def w(x,y):
    return (x+y)/2


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
                        #print(str(poids) + ' = poids, count_voisin =' + str(count_voisin))
            if (count_voisin >0 and uniform(0,1)<(p_infect*poids)/count_voisin):
                X[i] = True

def vaccin_rand(m, matrix, mu_vaccin):
    n = len(matrix)
    X = [True for i in range(n)]
    l_n = [i for i in range(n)]
    shuffle(l_n)
    count = 0 #count number of people vaccinated
    itera = 0
    while count != m:
        i = l_n[itera%n]
        itera += 1
        if (uniform(0,1) < mu_vaccin):
            X[i] = False
            count += 1
            for k in range(len(matrix)):
                if (matrix[i][k]>0):
                    matrix[i][k] = 0
                    matrix[k][i] = 0
    return X
