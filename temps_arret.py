from generation_matrice import gen_matrix, transition, w, uniform, vaccin_rand

def simulation(n_pop, p_heal, p_infect, X, graph):
    healed = False
    counter = 0
    while(not healed):
        transition(graph, X, p_heal, p_infect)
        healed = True
        test= 0
        for j in X:
            healed = healed and not j
            if not j:
                test += 1
        counter += 1
     return counter


def moyenne_ta(n_tests, n_pop, p_heal, p_infect, graph):
    s = 0
    mu_vaccin = 0.5
    X = vaccin_rand(0, graph, mu_vaccin)
    for i in range(n_tests):
        s += simulation(n_pop, p_heal, p_infect, X, graph)
    print("fini ...")
    return s/n_tests

def main(N, n_test, p_heal, p_infect, graph):
    """
    Main effectue le test sur graph, renvoie la moyenne et variance en fonction du nombre de personne vaccine
    """
    est_moy = 0
    list_moy = []
    var = 0
    for n in range(n_test):
        m_i = moyenne_ta(n_test, N, p_heal, p_infect, graph)
        list_moy.append(m_i)
        est_moy += m_i
    est_moy = est_moy/n_test
    for n in range(n_test):
        var += (est_moy - est_moy)**2
    var = var/n_test
    print("fini")
    return (est_moy, pow(var, 1/2))
