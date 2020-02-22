from generation_matrice import gen_matrix, transition, w, uniform, vaccin_rand
from page_ranking import page_ranking, plus_grand_degres, vaccine
import numpy as np
from graphic import affiche_graph
import matplotlib.pyplot as plt


## Tant que toute la population n'est pas entièrement guérie, on 
def simulation(n_pop, p_heal, p_infect, X, graph):
    healed = False
    counter = 0
    affiche_graph(graph, X, [])
    while(not healed):
        infected = transition(graph, X, p_heal, p_infect)
        print(infected)
        healed = True
        for j in X:
            healed = healed and not j
        counter += 1
        #print(X)
        plt.clf()
        slow = affiche_graph(graph, X, infected)
        if slow:
            plt.pause(0.1)
        else:
            plt.pause(10)
        print('boo')
    affiche_graph(graph, X, [])
    plt.show()
    return counter


def moyenne_ta_alea(n_tests, n_pop, p_heal, p_infect, graph, nb_vacc):
    s = 0
    mu_vaccin = 0.5
    X = vaccin_rand(nb_vacc, graph, mu_vaccin)
    for i in range(n_tests):
        s += simulation(n_pop, p_heal, p_infect, X, graph)
    print("fini ...")
    return s/n_tests

### On code une fonction propre à chaque méthode car des subtilités sont propres à certaines méthodes
### Par exemple, on doit boucler deux fois pour la méthode aléatoire car on a de l'aléatoire à deux endroits


def main_alea(N, n_test, p_heal, p_infect, graph):
    """
    Main effectue le test sur graph, renvoie la moyenne et variance en fonction du nombre de personne vaccine pour la methode aleatoire
    """
    est_moy = 0
    list_moy = []
    var = 0
    for n in range(n_test):
        m_i = moyenne_ta(n_test, N, p_heal, p_infect, graph)
        list_moy.append(m_i)
        est_moy += m_i
    est_moy = est_moy/n_test
    for i in range(n_test):
        var += (list_moy[i] - est_moy)**2
    var = var/n_test
    print("fini")
    return (est_moy, pow(var, 1/2))

def main_pg_v1(N,n_test, p_heal, p_infect, graph, nb_vacc, Xm):
    est_moy = 0
    list_el = []
    var = 0
    graph_copie = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            graph_copie[i][j] = graph[i][j]
    page_ranking(graph_copie, nb_vacc, Xm, 0.1)
    X_save = [Xm[i] for i in range(N)]
    for n in range(n_test):
        X = [X_save[i] for i in range(N)]
        s_i = simulation(N, p_heal, p_infect, X, graph_copie)
        list_el.append(s_i)
        est_moy += s_i
    est_moy = est_moy/n_test
    for i in range(n_test):
        var += (list_el[i] - est_moy)**2
    var = var/n_test
    return est_moy, var,  X_save

def main_pg_v2(N,n_test, p_heal, p_infect, graph, nb_vacc, Xm):
    est_moy = 0
    list_el = []
    var = 0
    graph_copie = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            graph_copie[i][j] = graph[i][j]
            
    page_ranking(graph, 1, Xm, 0.1)
    X_save = [Xm[i] for i in range(N)]
    for n in range(n_test):
        X = [X_save[i] for i in range(N)]
        #s_i = simulation(N, p_heal, p_infect, X, graph_copie)
        s_i = simulation(N, p_heal, p_infect, X, graph)
        list_el.append(s_i)
        est_moy += s_i
    est_moy = est_moy/n_test
    for i in range(n_test):
        var += (list_el[i] - est_moy)**2
    var = var/n_test
    return est_moy, var,  X_save

def main_pgd(N,n_test, p_heal, p_infect, graph, nb_vacc, Xm):
    est_moy = 0
    list_el = []
    var = 0
    graph_copie = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            graph_copie[i][j] = graph[i][j]
            
    plus_grand_degres(graph, 1, Xm, 0.1)
    X_save = [Xm[i] for i in range(N)]
    for n in range(n_test):
        X = [X_save[i] for i in range(N)]
        s_i = simulation(N, p_heal, p_infect, X, graph)
        list_el.append(s_i)
        est_moy += s_i
    est_moy = est_moy/n_test
    for i in range(n_test):
        var += (list_el[i] - est_moy)**2
    var = var/n_test
    return est_moy, var,  X_save

def main_glouton(N, n_test, p_heal, p_infect, graph, X):
    temps_min = 100000000
    var_min = 0
    i_min = 0
    for i in range(N):
        if X[i]:
            print(i)
            graph_copie = np.zeros((N,N))
            for j in range(N):
                for k in range(N):
                    graph_copie[j][k] = graph[j][k]
            Xs = [X[i] for i in range(N)]
            vaccine(graph_copie, i, Xs)
            X_save = [Xs[i] for i in range(N)]
            est_moy = 0
            list_el = []
            var = 0
            for n in range(n_test):
                Xss = [X_save[i] for i in range(N)]
                s_i = simulation(N, p_heal, p_infect, Xss, graph)
                list_el.append(s_i)
                est_moy += s_i
            est_moy = est_moy/n_test
            for j in range(n_test):
                var += (list_el[j] - est_moy)**2
            var = var/n_test
            if(est_moy < temps_min):
                i_min = i
                temps_min = est_moy
                var_min = var
    vaccine(graph, i_min, X)
    return temps_min, var, X
        

## on teste l'influence d'une vaccination particulière (vacc ici), cela sert pour le cycle
## car on gènere à la main les différrentes vaccinations possibles 
def main_cycle(N,n_test, p_heal, p_infect, graph, vacc, Xm):
    est_moy = 0
    list_el = []
    var = 0
    graph_copie = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            graph_copie[i][j] = graph[i][j]
            
    X = [Xm[i] for i in range(len(Xm))]
    for i in vacc:
        vaccine(graph_copie, i, X)
    
    X_save = [X[i] for i in range(N)]
    for n in range(n_test):
        X = [X_save[i] for i in range(N)]
        s_i = simulation(N, p_heal, p_infect, X, graph_copie)
        list_el.append(s_i)
        est_moy += s_i
    est_moy = est_moy/n_test
    for i in range(n_test):
        var += (list_el[i] - est_moy)**2
    var = var/n_test
    return est_moy, var,  X_save

