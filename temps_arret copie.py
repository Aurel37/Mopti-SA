from generation_matrice import gen_matrix, transition, w, uniform, vaccin_rand
import multiprocessing
import matplotlib.pyplot as plt
from graphic import affiche_graph

dt = 1/50

def simulation(n_pop, p_heal, p_infect, X, graph):
    healed = False
    counter = 0
    while(not healed):
        transition(graph, X, p_heal, p_infect)
        healed = True
        test = 0
        for j in X: 
            healed = healed and not j
            if not j:
                test += 1
        if (counter+1)%5 == 0:
            affiche_graph(graph, X)
            plt.pause(dt)
 
        counter += 1
    return counter 


def moyenne_ta(n_tests, n_pop, p_heal, p_infect, graph):
    s = 0
    mu_vaccin = 0.5
    X = vaccin_rand(0, graph, mu_vaccin)
    pool = multiprocessing.Pool(4)
    liste = [[n_pop, p_heal, p_infect, X, graph] for _ in range(n_tests)]
    res = pool.map(simulation, liste)
    for i in res:
        s += i
    return s/n_tests

def main(N,n_test, p_heal, p_infect, graph):
    s = 0
    for n in range(1):
        s += moyenne_ta(n_test, N, p_heal, p_infect, graph)
    print("fini")
    return s/n_test
