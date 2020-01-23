import networkx as nx
import matplotlib.pyplot as plt


def affiche_graph(Link_mat, X_vac=[]):
    n = len(Link_mat)
    Graph_print = nx.Graph()
    Graph_print.add_nodes_from([i for i in range(n)])
    for i in range(n):
        for j in range(n):
            if Link_mat[i][j] == 1:
                Graph_print.add_edge(i, j)
    #plt.plot(121)
    nx.draw(Graph_print, with_labels=True, font_weight='bold')
    #plt.show()
