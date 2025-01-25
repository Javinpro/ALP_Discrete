# Graph Operations and Visualization Tool

This Python program provides an easy-to-use tool for creating, analyzing, and visualizing graphs. The code utilizes the `networkx` library for graph operations and `matplotlib` for graph visualization. Below is a guide to understanding and using the tool effectively.

## Features
1. **Add Nodes and Edges**: Easily create nodes and edges for your graph, with optional weights on edges.
2. **Visualize Graph**: Display the graph visually with nodes and edges clearly labeled.
3. **Find Shortest Path**: Calculate and visualize the shortest path between two nodes.
4. **Graph Properties**: Check if the graph is connected, calculate node degrees, clustering coefficients, and all-pairs shortest paths.
5. **Graph Diameter**: Calculate the diameter of the graph, representing the longest shortest path between two nodes.

## Prerequisites
- Python 3.8 or later.
- Required Python libraries:
  - `networkx`
  - `matplotlib`

You can install the dependencies using the following command:
```bash
pip install networkx matplotlib
```

## How to Use
### 1. Initialization
Create an instance of the `GraphOperations` class:
```python
from graph_operations import GraphOperations

graph = GraphOperations()
```

### 2. Add Nodes
Add nodes to the graph:
```python
graph.add_node(1)
graph.add_node(2)
```

### 3. Add Edges
Add edges between nodes, with an optional weight:
```python
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(2, 3, weight=2.3)
```

### 4. Visualize the Graph
Display the current graph:
```python
graph.visualize_graph()
```

### 5. Find and Visualize the Shortest Path
Calculate and print the shortest path between two nodes:
```python
graph.shortest_path(1, 3)
```
Visualize the shortest path:
```python
graph.visualize_shortest_path(1, 3)
```

### 6. Check Graph Connectivity
Check if the graph is connected:
```python
graph.is_connected()
```

### 7. Calculate Node Degree
Find the degree of a specific node:
```python
graph.degree_of_node(1)
```

### 8. Calculate Clustering Coefficients
Get the clustering coefficient for each node:
```python
graph.clustering_coefficient()
```

### 9. Find All-Pairs Shortest Paths
Calculate the shortest paths between all pairs of nodes:
```python
graph.all_pairs_shortest_path()
```

### 10. Calculate Graph Diameter
Determine the diameter of the graph:
```python
graph.diameter()
```

## Example Execution
Below is an example of how to use the tool:
```python
if __name__ == "__main__":
    graph = GraphOperations()

    # Add nodes and edges
    for node in [1, 2, 3, 4, 5]:
        graph.add_node(node)

    edges = [
        (1, 2, 4.5),
        (1, 3, 3.2),
        (2, 4, 2.7),
        (3, 4, 1.8),
        (1, 4, 6.7),
        (3, 5, 2.7)
    ]
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    # Visualize the graph
    graph.visualize_graph()

    # Find and visualize the shortest path
    graph.shortest_path(1, 5)
    graph.visualize_shortest_path(1, 5)

    # Other graph properties
    graph.is_connected()
    graph.degree_of_node(1)
    graph.clustering_coefficient()
    graph.all_pairs_shortest_path()
    graph.diameter()
```

## Output
- A visual representation of the graph.
- Printed information about shortest paths, connectivity, clustering coefficients, and more.


