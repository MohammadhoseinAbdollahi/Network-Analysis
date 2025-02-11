import networkx as nx

def degree_centrality(G):
    return nx.degree_centrality(G)

def betweenness_centrality(G):
    return nx.betweenness_centrality(G)

def closeness_centrality(G):
    return nx.closeness_centrality(G)
