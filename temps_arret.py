from generation_matrice import gen_matrix, transition, w, uniform

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

def moyenne_ta(n_tests, n_pop, p_heal, p_infect, X, graph):
    s = 0
    for i in range(n_tests):
        s += simulation(n_pop, p_heal, p_infect, X, graph)
    return s/n_tests
