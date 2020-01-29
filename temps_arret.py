from generation_matrice import gen_matrix, transition, w, uniform, vaccin_rand
from page_ranking import page_ranking

def simulation(n_pop, p_heal, p_infect, X, graph):
    healed = False
    counter = 0
    X_healed = [X[i] for i in range(len(X))]
    
    while(not healed):
        transition(graph, X, p_heal, p_infect, X_healed)
        healed = True
        for j in X:
            healed = healed and not j
        counter += 1
    return counter

def moyenne_ta_alea(n_tests, n_pop, p_heal, p_infect, graph, nb_vacc):
    s = 0
    mu_vaccin = 0.5
    X = vaccin_rand(nb_vacc, graph, mu_vaccin)
    for i in range(n_tests):
        s += simulation(n_pop, p_heal, p_infect, X, graph)
    print("fini ...")
    return s/n_tests

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

def main(N,n_test, p_heal, p_infect, graph, nb_vacc):
    est_moy = 0
    list_el = []
    var = 0
    X = [True for i in range(N)]
    page_ranking(graph, nb_vacc, X, 0.1)
    for n in range(n_test):
        s_i = simulation(N, p_heal, p_infect, X, graph)
        list_el.append(s_i)
        est_moy += s_i
    est_moy = est_moy/n_test
    for i in range(n_test):
        var += (list_el[i] - est_moy)**2
    var = var/n
    return [est_moy, pow(var, 1/2)]
