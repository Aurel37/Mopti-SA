from generation_matrice import gen_matrix, transition, w, uniform
def simulation(n_pop, p_heal, p_infect, p_sick, W):
    X = []
    for i in range(n_pop):
        if (uniform(0,1)<p_sick):
            X.append(True)
        else:
            X.append(False)
    graph  = gen_matrix(n_pop, W)
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
        #print(counter)
        #print('On a guérit '+ str(test)+' sur ' + str(n_pop))
    return counter 

def moyenne_ta(n_tests, n_pop, p_heal, p_infect, p_sick, W):
    s = 0
    for i in range(n_tests):
        #print(s)
        s += simulation(n_pop, p_heal, p_infect, p_sick, W)
        #print('Guerrrrrrrrrrrrrrrit')
    return s/n_tests
