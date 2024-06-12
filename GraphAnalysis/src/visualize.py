import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def plot_degree_distribution(degree_sequence):
    plt.loglog(degree_sequence, 'b-', marker='o')
    plt.title("Degree rank plot")
    plt.xlabel("Rank")
    plt.ylabel("Degree")
    plt.show()

def visualize_graph(G):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=50, node_color='blue', edge_color='gray')
    plt.show()

def visualize_communities(G, communities):
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(communities)))
    for community, color in zip(communities, colors):
        nx.draw_networkx_nodes(G, pos, nodelist=list(community), node_color=[color]*len(community), node_size=50)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.title("Network with Communities")
    plt.show()
