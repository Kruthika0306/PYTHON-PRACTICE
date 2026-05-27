import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("Python", "AI"),
    ("Python", "Data Science"),
    ("AI", "Machine Learning"),
    ("ML", "Deep Learning")
])

nx.draw(
    G,
    with_labels=True,
    node_size=3000
)

plt.show()

