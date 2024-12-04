import networkx as nx
import matplotlib.pyplot as plt

# Crea el grafo
G = nx.Graph()

# Agrega los nodos
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Agrega las relaciones entre los nodos
G.add_edge('A', 'B')  # A1 -> B
G.add_edge('A', 'C')  # A2 -> C
G.add_edge('B', 'C')  # B1 -> C

# Visualiza el grafo
nx.draw(G, with_labels=True)
#plt.show()
plt.savefig('grafo.png', dpi=100)
