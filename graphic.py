import networkx as nx
#import matplotlib.pyplot as plt
import generation_matrice as gen
import numpy as np



def affiche_graph(Link_mat, X, infected, healed):
    n = len(Link_mat)
    Graph_print = nx.Graph()
    node_col = []
    width_edge = []
    # Suivant l'état de chaque individu, on colorie les noeuds d'une certaine couleur
    for i in range(len(X)):
        Graph_print.add_node(i)
        if X[i]:
            if i in infected:
                node_col.append((0.8, 0.8, 0.1))
            else:
                node_col.append('red')
        else:
            if i in healed:
                node_col.append('blue')
            else:
                node_col.append('green')
    # Si un individu est contaminé, il contamine ses voisins. Ainsi, il y a des liaisons saines et d'autres à risque
    edge_col = []
    for i in range(n):
        for j in range(i,n):
            if X[i] or X[j]:
                edge_col.append('red')
            else:
                edge_col.append('green')
                
            if Link_mat[i][j] == 1 or i==j:
                if (i in infected and X[j]) or (j in infected and X[i]):
                    width_edge.append(5)
                    Graph_print.add_edge(i, j)
                    
                else:
                    width_edge.append(1)
                    Graph_print.add_edge(i, j)
            else:
                Graph_print.add_edge(i,j)
                width_edge.append(0)
    # On trace le graphe
    nx.draw_shell(Graph_print, width = width_edge, node_color = node_col, edge_color = edge_col, with_labels=True, font_weight='bold')
