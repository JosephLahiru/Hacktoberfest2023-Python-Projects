import networkx as nx
import matplotlib.pyplot as plt

num_nodes = 50  
probability = 0.2 

G = nx.gnp_random_graph(num_nodes, probability)

# Visualize the graph
pos = nx.spring_layout(G, seed=50)  
nx.draw(G, pos, with_labels=True, node_size=400, node_color='yellow', font_size=8)
plt.title("Gilbert Random Graph")
plt.show()

