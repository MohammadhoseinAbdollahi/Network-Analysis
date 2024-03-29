import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml('/Users/mohammadhosein/Library/CloudStorage/OneDrive-unige.it/SEM2-2024/NA/football/football.gml')
# Create a mapping from the current node names to numbers
mapping = {node: i for i, node in enumerate(G.nodes())}

# Create a new graph H that is the same as G but with the nodes relabeled
H = nx.relabel_nodes(G, mapping)


betweenness_centrality = nx.betweenness_centrality(G)


closeness_centrality = nx.closeness_centrality(G)


# Save the values to a text file
with open('/Users/mohammadhosein/Library/CloudStorage/OneDrive-unige.it/SEM2-2024/NA/ex2/centrality_values.txt', 'w') as file:
    file.write("Betweenness Centrality:\n")
    for node, value in betweenness_centrality.items():
        file.write(f"{node}: {value}\n")

    file.write("\nCloseness Centrality:\n")
    for node, value in closeness_centrality.items():
        file.write(f"{node}: {value}\n")

# Create figure and axes
# Compute the betweenness centrality of H
betweenness_centrality = nx.betweenness_centrality(H)

# Compute the closeness centrality of H
closeness_centrality = nx.closeness_centrality(H)
fig, ax = plt.subplots(2)

# Plot betweenness centrality
ax[0].bar(betweenness_centrality.keys(), betweenness_centrality.values())
ax[0].set_title('Betweenness Centrality')

# Plot closeness centrality
ax[1].bar(closeness_centrality.keys(), closeness_centrality.values())
ax[1].set_title('Closeness Centrality')

# Show the plot
plt.show()

