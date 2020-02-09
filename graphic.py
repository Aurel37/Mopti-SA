import networkx as nx
import matplotlib.pyplot as plt
import generation_matrice as gen
import numpy as np



def affiche_graph(Link_mat, X):
    n = len(Link_mat)
    Graph_print = nx.Graph()
    node_col = []
    for i in X:
        if i:
            node_col.append('red')
        else:
            node_col.append('green')
    print('size', len(node_col))
    edge_col = []
    for i in range(n):
        for j in range(n):
            if X[i] or X[j]:
                edge_col.append('green')
            else:
                edge_col.append('red')
    for i in range(n):
        for j in range(n):
            if Link_mat[i][j] == 1 or i==j:
                Graph_print.add_edge(i, j)
    #plt.plot(121)
    nx.draw(Graph_print, node_color = node_col, with_labels=True, font_weight='bold')
    plt.show()

#Link_mat = [[1 for i in range(10)] for _ in range(10)]
Link_mat = np.array([
       [0., 0., 1., 1., 0., 0., 1],
       [0., 0., 1., 1., 0., 1., 1],
       [1., 1., 0., 1., 0., 0., 0],
       [1., 1., 1., 0., 0., 0., 0],
       [0., 0., 0., 0., 0., 1., 1],
       [0., 1., 0., 0., 1., 0., 1],
       [1., 1., 0., 0., 1., 1., 0]
       ])

    
X = [False for _ in range(10)]
affiche_graph(Link_mat, X)
