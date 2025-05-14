from pyvis.network import Network

# Create a Pyvis Network
net = Network(notebook=False)

# Add nodes
net.add_node("A", label="Node A")
net.add_node("B", label="Node B")
net.add_node("C", label="Node C")

# Add edges
net.add_edge("A", "B")
net.add_edge("B", "C")
net.add_edge("C", "A")

# Save and show the graph
net.show("dist/simple_graph1.html", notebook=False)