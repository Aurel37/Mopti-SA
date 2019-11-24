from generation_matrice import gen_matrix, transition, w, uniform

def simulation(n_step, n_pop, p_heal, p_infect, p_sick, W):
    X = []
    for i in range(n_pop):
        if (uniform(0,1)<p_sick):
            X.append(True)
        else:
            X.append(False)
    print(n_pop)
    graph  = gen_matrix(n_pop, W)
    for i in range(n_step):
        transition(graph, X, p_heal, p_infect, p_sick)
        print(X)
    return X

simulation(10, 5,  0.5, 0.3, 0.7, w)
