from generation_matrice import gen_matrix, transition, w, uniform, vaccin_rand
from page_ranking import page_ranking

def simulation(n_pop, p_heal, p_infect, X, graph):
    healed = False
    counter = 0
    while(not healed):
        transition(graph, X, p_heal, p_infect)
        healed = True
        for j in X:
            healed = healed and not j
        counter += 1
        print(counter)

    return counter 

def moyenne_ta_alea(n_tests, n_pop, p_heal, p_infect, graph, nb_vacc):
    s = 0
    mu_vaccin = 0.5
    X = vaccin_rand(nb_vacc, graph, mu_vaccin)
    for i in range(n_tests):
        print(i)
        s += simulation(n_pop, p_heal, p_infect, X, graph)
    print("fini ...")
    return s/n_tests

def vaccin_rank(n_tests, n_pop, p_heal, p_infect, graph, nb_vacc):

def main(N,n_test, p_heal, p_infect, graph, nb_vacc):
    s = 0
    for n in range(n_test):
        s += moyenne_ta_alea(n_test, N, p_heal, p_infect, graph, nb_vacc)
    print("fini")
    return s/n_test
