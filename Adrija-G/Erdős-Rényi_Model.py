import networkx as nx
import matplotlib.pyplot as plt

num_nodes = 20
probability = 0.2

G = nx.erdos_renyi_graph(num_nodes, probability)

pos = nx.spring_layout(G, seed=42)  
nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=8)
plt.title("Erdős-Rényi Random Graph")
plt.show()
