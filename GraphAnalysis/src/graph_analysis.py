import networkx as nx
def graph_info(G):
    info = nx.info(G)
    return info

def degree_distribution(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    return degree_sequence

def average_path_length(G):
    if nx.is_connected(G):
        return nx.average_shortest_path_length(G)
    else:
        largest_cc = max(nx.connected_components(G), key=len)
        subgraph = G.subgraph(largest_cc)
        return nx.average_shortest_path_length(subgraph)

def clustering_coefficient(G):
    return nx.average_clustering(G)

def density(G):
    return nx.density(G)
