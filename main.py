from temps_arret import *
import numpy as np
import matplotlib.pyplot as plt
from generation_matrice import gen_matrix, w
from page_ranking import *
from graphic import affiche_graph

N = 30
l = 0.5
mu = 0.2
dt = 0.1
ntests = 5000


X = [i for i in range(0, 11)]
Y = [i for i in range(0, 11)]
Yerr = []
Xvacc = [True for i in range(N)]
graph = gen_matrix(N, w)
graph_circulaire = np.zeros((N,N))
for i in range(N): 
        if (i!=N-1):
            graph_circulaire[i][i+1] = 1
            graph_circulaire[i+1][i] = 1
        elif (i==N-1):
            graph_circulaire[i][0] = 1
            graph_circulaire[0][i] = 1

X_test = [True for i in range(N)]

affiche_graph(graph_circulaire, X_test)

page_ranking(graph_circulaire, 6, X_test)
print(len(X_test), X_test)

affiche_graph(graph_circulaire, X_test)

graph_ligne =  np.zeros((N,N))
for i in range(N):
    if (i!=N-1):
        graph_ligne[i][i+1] = 1

affiche_graph(graph_ligne, X_test)

graph_copie = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        graph_copie[i][j] = graph[i][j]

graph_copi = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        graph_copi[i][j] = graph[i][j]
##plus_grand_degres(graph, 10, Xvacc)
##page_ranking(graph_copie, 10, Xvacc)
        
Xm = [True for _ in range(N)]

#for i in range(len(X)):
#    print(i)
#    #res = main_glouton(N, ntests, l*dt, mu*dt, graph, Xm)
#    res = main(N, ntests, l*dt, mu*dt, graph, X[i])
#    Y[i] = res[0]
#    Sn = res[1]
#    Snp = 2.58 * np.sqrt(Sn)/np.sqrt(ntests)
#    Yerr.append(Snp)

#plt.errorbar(X, Y, yerr = Yerr)
        
##Y1 = [86.047, 85.098, 84.931, 83.831, 82.651, 82.195, 80.791, 79.426, 78.01, 76.675, 74.667]
##Yerr1 = [2.2362704071762867, 2.385403919093871, 2.4447692166510113, 2.464653556797872, 2.4746756629842244, 2.393568349584861, 2.408455833026963, 2.426152167933742, 2.3241591727848605, 2.2685485348565897, 2.1646652018045645]
##
##Y2 =  [86.047, 84.873, 85.341, 84.091, 82.267, 82.64, 81.303, 81.808, 81.397, 78.468, 79.551]
##Yerr2 = [2.2362704071762867, 2.222416359399023, 2.35655668914448, 2.292911361294107, 2.2962401650307402, 2.170941456087655, 2.169317009330907, 2.3165772962865723, 2.2143997232325523, 2.021246783707126, 2.05762626468064]
##Y3 = [86.649, 86.322, 84.308, 83.624, 81.888, 81.932, 80.136, 80.579, 80.626, 80.773, 77.9]
##
##Yerr3 = [2.350862530830673, 2.435391975067337, 2.266046673497791, 2.2558741973775045, 2.2109854225929215, 2.1382105103114624, 2.0164932476022837, 2.082022848627651, 2.187335083199099, 2.1395177481770067, 1.9935171006038546]
##plt.errorbar(X, Y1, Yerr1, label = "Glouton")
##plt.errorbar(X, Y2, Yerr2, label = "plus grand degre")
##plt.errorbar(X, Y3, Yerr3, label = "page ranking")
##plt.legend()

#plt.show()
