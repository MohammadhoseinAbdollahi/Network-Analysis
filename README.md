# Network Analysis Exercises
 
This repository contains a series of exercises designed to familiarize you with the NetworkX library for network analysis and graph theory. Each exercise builds on the previous one, covering various aspects of graph properties, centrality measures, random graph models, and synthetic graph models.

## Prerequisites

- Install NetworkX: Follow the [NetworkX documentation](https://networkx.org/documentation/stable/index.html) for installation instructions.

## Exercises

### Exercise 1: Warm Up

1. **Select a Graph**: Choose a graph from the [NetworkX examples](https://networkx.org/documentation/stable/auto_examples/index.html#graph).
2. **Compute and Print Basic Properties**: Determine and display the number of nodes, number of links, diameter, and adjacency list of the graph.
3. **Draw the Graph**: Visualize the graph.
4. **Plot Degree Distribution**: Create a plot showing the degree distribution.

**Repeat Steps 1-4** using a graph loaded from an external file (datasets available at [Network Repository](https://networkrepository.com/)).

### Exercise 2: Betweenness and Closeness

1. **Use the Graph from Exercise 1**.
2. **Compute Centrality Measures**:
    - Betweenness Centrality
    - Closeness Centrality
3. **Print Top-10 Nodes**: For each metric, display the top-10 nodes and their associated centrality values.

**Repeat Steps 1-3** using a graph loaded from an external file (datasets available at [Network Repository](https://networkrepository.com)).

### Exercise 3: Erdős-Rényi Random Graphs

1. **Generate Erdős-Rényi Graphs**: Create different Erdős-Rényi random graphs \( G(N, p) \) by varying the number of vertices \( N \) and the probability \( p \).
2. **Compute Metrics and Connectivity**: For each graph, compute basic metrics and check if it is connected. If connected, compute its diameter.
3. **Plot Degree Distribution**: Visualize the degree distribution of each graph.

### Exercise 4: Erdős-Rényi Random Graphs (Continued)

1. **Expected Number of Links**: Calculate the expected number of links \( \langle L \rangle \).
2. **Network Regime**: Determine the regime of the network.
3. **Critical Probability \( p_c \)**: Compute the probability \( p_c \) so that the network is at the critical point.
4. **Critical Number of Nodes \( N_{cr} \)**: Calculate the number of nodes \( N_{cr} \) so that the network has only one component given \( p = 10^{-3} \).
5. **Average Degree and Distance**: For the network in step 4, calculate the average degree \( \langle k_{cr} \rangle \) and the average distance \( \langle d \rangle \) between two randomly chosen nodes.

### Exercise 5: Regular Graphs and Watts-Strogatz Model

#### Regular Graphs

1. **Choose Regular Graphs**: For example, a complete graph (clique) or a triangular lattice.
2. **Compute Metrics**: Calculate the diameter, number of triangles, transitivity, and clustering coefficient.
3. **Plot Degree Distribution**: Visualize the degree distribution.

#### Triangular Lattice

1. **Triangular Lattice Visualization**: Obtain and interpret the triangular lattice graph.
2. **Degree Distribution**: Analyze and interpret the degree distribution.
3. **Metrics**:
    - Number of nodes: 2626
    - Number of edges: 7625
    - Min degree: 2
    - Max degree: 6
    - Transitivity: 0.40297665421916556
    - Average clustering: 0.41254125412540116

**Note**: NetworkX provides basic functionality for visualizing graphs. Future visualization functionality may be removed or made available as an add-on package. See [NetworkX drawing documentation](https://networkx.org/documentation/stable/reference/drawing.html).

#### Watts-Strogatz Model

1. **Reuse Code from Regular Graphs**: Apply the code developed for regular graphs to the Watts-Strogatz model using a circle layout.
2. **Compare with \( G(N, M) \)**: Generate two random graphs with the same number of nodes \( N \) and links \( M \) and compare their characteristics.

### Exercise 6: Configuration and Barabási-Albert Models

#### Configuration Model

1. **Define Degree Sequence**: Create a degree sequence.
2. **Create MultiGraph**: Generate a random pseudograph matching the degree sequence.
3. **Remove Self Loops**: Use `remove_edges_from()` and `selfloop_edges()`.
4. **Remove Multi Edges**: Convert to a simple graph.
5. **Print Information**: Display information about the resulting graphs.

**Repeat from Step 1** with different degree sequences.

#### Barabási-Albert Model

1. **Generate Networks**: Create Barabási-Albert networks for different parameters.
2. **Compute Metrics**: Measure the degree of important hubs, global clustering, and diameter.
3. **Degree Distribution**: Analyze the histogram and plot in log-log scale.

## Additional Information

For more details and usage of the NetworkX library, refer to the [NetworkX documentation](https://networkx.org/documentation/stable/index.html).

Feel free to contribute to this repository by adding new exercises or improving existing ones.
