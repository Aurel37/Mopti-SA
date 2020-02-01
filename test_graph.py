import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_node(1,color='red',style='filled',fillcolor='blue',shape='square')
G.add_node(2,color='blue',style='filled')
G.add_edge(1,2,color='green')
G.nodes[2]['shape']='circle'
G.nodes[2]['fillcolor']='red'
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
