import networkx as nx
import json

def load_graph(edge_file, json_file):
    G = nx.read_edgelist(edge_file, delimiter=' ')
    with open(json_file) as f:
        metadata = json.load(f)
    for node in G.nodes():
        if node in metadata:
            G.nodes[node]['genres'] = metadata[node]
    return G
