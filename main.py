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
    print(graph)
    heal_itself = [0 for i in range(n_pop)]
    for i in range(n_step):
        transition(graph, X, p_heal, p_infect, heal_itself)
        print(X)
    return X

simulation(20, 30,  0.2, 0.5, 1, w)
