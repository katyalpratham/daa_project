import tkinter as tk
from tkinter import messagebox
from dijkstra import Graph
import matplotlib.pyplot as plt
import networkx as nx

class DijkstraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Airport Navigation System")

        self.graph = Graph()

        self.node_label = tk.Label(root, text="Location(e.g,gate1 etc)")
        self.node_label.pack()

        self.node_entry = tk.Entry(root)
        self.node_entry.pack()

        self.add_node_button = tk.Button(root, text="Add Location", command=self.add_node)
        self.add_node_button.pack()

        self.edge_label = tk.Label(root, text="Path (start,end,Distance in meter):")
        self.edge_label.pack()

        self.edge_entry = tk.Entry(root)
        self.edge_entry.pack()

        self.add_edge_button = tk.Button(root, text="Add Path", command=self.add_edge)
        self.add_edge_button.pack()

        self.start_label = tk.Label(root, text="Start Location:")
        self.start_label.pack()

        self.start_entry = tk.Entry(root)
        self.start_entry.pack()

        self.find_path_button = tk.Button(root, text="Find Shortest Route", command=self.find_shortest_path)
        self.find_path_button.pack()

        self.plot_graph_button = tk.Button(root, text="Show Airport Layout", command=self.plot_graph)
        self.plot_graph_button.pack()

        self.result_text = tk.Text(root, height=10, width=40)
        self.result_text.pack()

    def add_node(self):
        node = self.node_entry.get().strip()
        if node:
            self.graph.add_node(node)
            messagebox.showinfo("Info", f"Location {node} added.")
            self.node_entry.delete(0, tk.END)

    def add_edge(self):
        edge_data = self.edge_entry.get().strip().split(',')
        if len(edge_data) == 3:
            start, end, weight = edge_data
            try:
                weight = int(weight)
                self.graph.add_edge(start.strip(), end.strip(), weight)
                messagebox.showinfo("Info", f"Edge from {start.strip()} to {end.strip()} with weight {weight} added.")
                self.edge_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Weight must be an integer.")
        else:
            messagebox.showerror("Error", "Please enter the edge in the format (start,end,weight).")

    def find_shortest_path(self):
        start = self.start_entry.get().strip()
        if start in self.graph.adjacency_list:
            distances = self.graph.dijkstra(start)
            result = "\n".join([f"Distance from {start} to {node}: {distances[node]}" for node in distances])
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        else:
            messagebox.showerror("Error", f"Node {start} not found in the graph.")

    def plot_graph(self):
        G = nx.Graph()

        for node in self.graph.adjacency_list:
            G.add_node(node)

        for start, edges in self.graph.adjacency_list.items():
            for end, weight in edges.items():
                G.add_edge(start, end, weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.title("Graph Visualization")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DijkstraApp(root)
    root.mainloop()