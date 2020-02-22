from temps_arret import *
import numpy as np
from generation_matrice import gen_matrix, w, w1
from page_ranking import *
from graphic import affiche_graph


N = 10
l = 0.5
mu = 0.5
dt = 0.1
ntests = 10000


graph_etoile = np.array([[0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 0., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 0., 1.],
       [0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 0., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 0., 1.],
       [1., 1., 0., 1., 1., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1.,
        0., 0., 1., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1.,
        0., 0., 1., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 1., 1., 1., 1., 1., 1.,
        0., 0., 1., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 1., 1., 1., 1., 1., 1.,
        0., 0., 1., 0., 1., 1., 1., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 1., 0., 0., 0.,
        0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 1., 0., 0., 0.,
        0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 1., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0.,
        0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1.,
        0., 0., 1., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 1.,
        0., 0., 1., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 0.,
        0., 0., 1., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 0., 0.],
       [0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1.,
        1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        1., 1., 0., 0., 1., 1., 1., 1., 0., 1., 1., 1., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 0., 0., 0., 1., 1., 1., 0., 1., 0., 0., 0., 0., 0., 0.,
        1., 1., 0., 1., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0.],
       [1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        1., 1., 0., 1., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0.],
       [0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 1.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1.,
        1., 1., 1., 1., 0., 0., 1., 1., 1., 0., 1., 1., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1.,
        1., 1., 1., 1., 0., 0., 1., 1., 1., 1., 0., 1., 0., 0.],
       [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 0., 1., 0., 1., 1., 1.,
        1., 1., 1., 1., 0., 0., 1., 1., 1., 1., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
       [1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 1., 0.]])

graph_exemple = np.array([[0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 1.,
        1., 0., 1., 1., 1., 1., 0., 0., 0., 1., 0., 0., 0., 1.],
       [1., 1., 1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 1., 1., 1., 0.,
        0., 1., 0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 1., 0.]])

graph_alea = gen_matrix(N, w)
Xvacc = [True for i in range(N)]
simulation(N, l*dt, mu*dt, Xvacc, graph_alea)
##graph_alea = gen_matrix(N, w)
##affiche_graph(graph_alea, Xvacc)
## Test pour le  graphe cyclique
##graph_cycle = np.zeros((N, N))
##for i in range(N):
##    graph_cycle[i][(i+1)%N]=1
##    graph_cycle[(i+1)%N][i]=1
## toutes les combinaisons possibles de vaccin 
##vacc = [[0,1], [0, 2], [0, 3], [0, 2, 3], [0, 2, 4], [0, 1, 2], [0, 1, 2, 3], [0, 2, 3, 5], [0, 1, 2, 4]]
##Xvacc = [True for i in range(N)]
##for v in vacc:
##    res = main_cycle(N, ntests, l*dt,  mu*dt, graph_cycle, v, Xvacc)
##    Sn = res[1]
##    Snp = 2.58 * np.sqrt(Sn)/np.sqrt(ntests)
##    print(res[0], Snp)
##    
##### Méthode sans modifier le graphe de base: Page_Ranking version 1
##
##for k in range(6):
##    graph_copie = np.zeros((N,N))
##    for i in range(N):
##        for j in range(N):
##            graph_copie[i][j] = graph[i][j]
##    page_ranking(graph_copie, k, Xvacc, 0.1)
##
##
##### Méthode avec modification du graph de base: Page_ranking version 2 et Plus grand degrè
##
##for k in range(6):
##    graph_copie = np.zeros((N,N))
##    for i in range(N):
##        for j in range(N):
##            graph_copie[i][j] = graph[i][j]
##            
##    #page_ranking(graph, 1, Xvacc, 0.1)
##    plus_grand_degres(graph, 1, Xvacc)
##
##
##### Traçage des comparaions des differentees méthodes:
##    
##X = [i for i in range(0, 11)]
##Y = [i for i in range(0, 11)]
##Yerr = []
##Xvacc = [True for i in range(N)]
##Xm = [True for _ in range(N)]
##
##for i in range(len(X)):
##    print(i)
##    #res = main_glouton(N, ntests, l*dt, mu*dt, graph, Xm)
##    res = main_pgd(N, ntests, l*dt, mu*dt, graph, X[i], Xm)
##    #res = main_pg_v2(N, ntests, l*dt, mu*dt, graph, X[i], Xm)
##    #res = main_pg_v1(N, ntests, l*dt, mu*dt, graph, X[i], Xm)
##    Y[i] = res[0]
##    Sn = res[1]
##    Snp = 2.58 * np.sqrt(Sn)/np.sqrt(ntests)
##    Xmm = res[2]
##    for j in range(N):
##        Xm[j] = Xmm[j]
##    Yerr.append(Snp)
##
##plt.errorbar(X, Y, yerr = Yerr)
