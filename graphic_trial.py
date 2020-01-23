import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
#nx.shortest_path(G, 'A', 'D', weight='weight')

plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
