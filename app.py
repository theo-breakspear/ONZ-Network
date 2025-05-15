from pyvis.network import Network
import webbrowser
import pandas
import itertools

df = pandas.read_csv("publications.csv")

authors = df['Name'].unique()

papers = df['Title'].unique()

authorList = {}

for paper in papers:
    paperAuthors = df.loc[df['Title'] == paper, 'Name'].tolist()
    if len(paperAuthors) > 1:
        authorList[paper] = paperAuthors

edgelist = []

for paper in authorList:
    edgelist += list(itertools.combinations(authorList[paper], 2))

# Create a Pyvis Network
net = Network(notebook=False)
net.barnes_hut(damping=0.5)

# Add nodes
for author in authors:
    net.add_node(author, label=author)

#Add edges
for edge in edgelist:
    net.add_edge(edge[0], edge[1])

# Save and show the graph
net.show("dist/simple_graph1.html", notebook=False)
webbrowser.open("dist/simple_graph1.html")

