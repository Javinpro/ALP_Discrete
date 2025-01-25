import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph

    def draw_graph(self, highlight_edges=None, title="Visualisasi Graf"):
        """Helper untuk menggambar graf secara visual."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=12, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        if highlight_edges:
            nx.draw_networkx_edges(self.graph, pos, edgelist=highlight_edges, edge_color='red', width=2)

        plt.title(title)
        plt.show()

class GraphOperations:
    def __init__(self):
        self.graph = nx.Graph()
        self.visualizer = GraphVisualizer(self.graph)

    def add_node(self, node):
        """Menambahkan simpul ke dalam graf."""
        self.graph.add_node(node)
        print(f"Simpul {node} telah ditambahkan.")

    def add_edge(self, u, v, weight=None):
        """Menambahkan sisi antara dua simpul."""
        self.graph.add_edge(u, v, weight=weight)
        print(f"Sisi ditambahkan antara {u} dan {v} dengan bobot {weight}.")

    def visualize_graph(self):
        """Menampilkan graf secara visual."""
        self.visualizer.draw_graph()

    def shortest_path(self, source, target):
        """Menghitung jalur terpendek antara dua simpul."""
        try:
            path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')
            print(f"Jalur terpendek dari {source} ke {target}: {path}")
            return path
        except nx.NetworkXNoPath:
            print(f"Tidak ada jalur dari {source} ke {target}.")
            return None

    def visualize_shortest_path(self, source, target):
        """Menampilkan visualisasi jalur terpendek antara dua simpul."""
        path = self.shortest_path(source, target)
        if path:
            path_edges = list(zip(path, path[1:]))
            self.visualizer.draw_graph(highlight_edges=path_edges, title=f"Jalur Terpendek dari {source} ke {target}")

    def is_connected(self):
        """Memeriksa apakah graf terhubung atau tidak."""
        connected = nx.is_connected(self.graph)
        print(f"Apakah graf terhubung? {connected}")
        return connected

    def degree_of_node(self, node):
        """Menghitung derajat dari simpul tertentu."""
        if node in self.graph:
            degree = self.graph.degree[node]
            print(f"Derajat dari simpul {node}: {degree}")
            return degree
        else:
            print(f"Simpul {node} tidak ditemukan di dalam graf.")
            return None

    def clustering_coefficient(self):
        """Menghitung koefisien clustering untuk setiap simpul."""
        clustering = nx.clustering(self.graph)
        print("Koefisien clustering untuk setiap simpul:")
        for node, coef in clustering.items():
            print(f"Simpul {node}: {coef:.2f}")
        return clustering

    def all_pairs_shortest_path(self):
        """Menghitung jalur terpendek antara semua pasangan simpul."""
        paths = dict(nx.all_pairs_shortest_path(self.graph))
        print("Jalur terpendek antara semua pasangan simpul:")
        for source, targets in paths.items():
            for target, path in targets.items():
                print(f"{source} -> {target}: {path}")
        return paths

    def diameter(self):
        """Menghitung diameter graf (jarak terpanjang antara dua simpul terdekat)."""
        try:
            dia = nx.diameter(self.graph)
            print(f"Diameter graf: {dia}")
            return dia
        except nx.NetworkXError as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    graph = GraphOperations()

    # Menambahkan simpul ke dalam graf
    for node in [1, 2, 3, 4, 5]:
        graph.add_node(node)

    # Menambahkan sisi dengan bobot ke dalam graf
    edges = [(1, 2, 4.5), (1, 3, 3.2), (2, 4, 2.7), (3, 4, 1.8), (1, 4, 6.7), (3, 5, 2.7)]
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    # Visualisasi graf
    graph.visualize_graph()

    # Menampilkan jalur terpendek
    graph.shortest_path(1, 5)

    # Visualisasi jalur terpendek
    graph.visualize_shortest_path(1, 5)

    # Memeriksa apakah graf terhubung
    graph.is_connected()

    # Menghitung derajat dari simpul tertentu
    graph.degree_of_node(1)

    # Menghitung koefisien clustering
    graph.clustering_coefficient()

    # Menampilkan semua jalur terpendek antara pasangan simpul
    graph.all_pairs_shortest_path()

    # Menghitung diameter graf
    graph.diameter()
