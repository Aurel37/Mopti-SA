import networkx as nx
import matplotlib.pyplot as plt


def affiche_graph(Link_mat,X):
    n = len(Link_mat)
    Graph_print = nx.Graph()
    node_col = ['green' if not i else 'red' for i in X]
    edge_col = []
    for i in range(n):
        for j in range(n):
            if X[i] or X[j]:
                edge_col.append('red')
            else:
                edge_col.append('green')
    for i in range(n):
        for j in range(n):
            if Link_mat[i][j] == 1:
                Graph_print.add_edge(i, j)
    #plt.plot(121)
    nx.draw(Graph_print, node_color = node_col, edge_color = edge_col, with_labels=True, font_weight='bold')
    plt.show()

Link_mat = [[1 for i in range(10)] for _ in range(10)]
X = [True for _ in range(10)]
affiche_graph(Link_mat, X)
