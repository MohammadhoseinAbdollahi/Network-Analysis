import itertools

import networkx as nx
from networkx.algorithms.community import girvan_newman

def detect_communities(G, k=5):
    communities = girvan_newman(G)
    limited_communities = list(itertools.islice(communities, k))
    return limited_communities
