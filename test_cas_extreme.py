from page_ranking import page_ranking, plus_grand_degres
import numpy as np
from graphic import affiche_graph

N = 8
nb_test = 500

graph_circulaire = np.zeros((N,N))

def copie_graph(G1, G2):
    for i in range(N):
        for j in range(N):
            G1[i][j] = G2[i][j]

X_test = [True for i in range(N)]

graph_ligne = np.zeros((N, N))
for i in range(N):
    if (i!=N-1):
        graph_ligne[i][i+1] = 1

plus_grand_degres(graph_ligne, 3,X_test)
print("test", X_test)

affiche_graph(graph_ligne,X_test)

for i in range(N): 
        if (i!=N-1):
            graph_circulaire[i][i+1] = 1
            graph_circulaire[i+1][i] = 1
        elif (i==N-1):
            graph_circulaire[i][0] = 1
            graph_circulaire[0][i] = 1

graph_copie_pr = np.zeros((N,N))



Edge_proba_0 = [0 for i in range(N)]

for i in range(nb_test):
    X_test = [True for i in range(N)]
    copie_graph(graph_copie_pr, graph_circulaire)
    page_ranking(graph_copie_pr, 3, X_test)
    #if (i==1):
    #    affiche_graph(graph_copie_pr, X_test)
    for j in range(N):
        if not(X_test[j]):
            Edge_proba_0[j] += 1/(3*nb_test)
print("page ranking : ", Edge_proba_0)

#affiche_graph(graph_circulaire, X_test)

Edge_proba_1 = [0 for i in range(N)]

for i in range(nb_test):
    X_test = [True for i in range(N)]
    copie_graph(graph_copie_pr, graph_circulaire)
    plus_grand_degres(graph_copie_pr, 3, X_test)
    #if (i==1):
    #    affiche_graph(graph_copie_pr, X_test)
    for j in range(N):
        if not(X_test[j]):
            Edge_proba_1[j] += 1/(3*nb_test)

print("plus grand degre : ", Edge_proba_1)

Edge_proba_2 = [0 for i in range(N)]


