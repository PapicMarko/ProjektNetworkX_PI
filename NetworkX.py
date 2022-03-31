#NetworkX.org

#Creating a graph
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

#Nodes
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])
H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)

#Edges
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*
G.add_edges_from([(1, 2), (1, 3)])
G.add_edges_from(H.edges)
G.clear()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')
G.number_of_nodes()
8
G.number_of_edges()
3
DG = nx.DiGraph()
DG.add_edge(2, 1)   # adds the nodes in order 2, 1
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)
assert list(DG.successors(2)) == [1, 4]
assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)]

#Examining elements of a graph
list(G.nodes)
[1, 2, 3, 'spam', 's', 'p', 'a', 'm']
list(G.edges)
[(1, 2), (1, 3), (3, 'm')]
list(G.adj[1])  # or list(G.neighbors(1))
[2, 3]
G.degree[1]  # the number of edges incident to 1
2
G.edges([2, 'm'])

G.degree([2, 3])

G.remove_node(2)
G.remove_nodes_from("spam")
list(G.nodes)
[1, 3, 'spam']
G.remove_edge(1, 3)
G.add_edge(1, 2)
H = nx.DiGraph(G)   # create a DiGraph using the connections from G
list(H.edges())
[(1, 2), (2, 1)]
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)

#Drawing graphs



G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()

options = {
    'node_color': 'red',
    'node_size': 50,
    'width': 2,
}
subax1 = plt.subplot(221)
nx.draw_random(G, **options)
subax2 = plt.subplot(222)
nx.draw_circular(G, **options)
subax3 = plt.subplot(223)
nx.draw_spectral(G, **options)
subax4 = plt.subplot(224)
nx.draw_shell(G, nlist=[range(5,10), range(5)], **options)

G = nx.dodecahedral_graph()
shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
nx.draw_shell(G, nlist=shells, **options)

plt.show()

nx.draw(G)
plt.savefig("path.png")



G = nx.Graph()
G.add_node(1)

#Adding nodes from any container

G.add_nodes_from([2, 3])
G.add_nodes_from(range(50, 110))
H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_node(H)
G.add_edge(1, 2)
G.add_edges_from([(1, 2), (1, 3)])
G.add_edges_from(H.edges)

plt.show()

class ThinGraph(nx.Graph):
    all_edge_dict = {"weight": 1}

    def single_edge_dict(self):
        return self.all_edge_dict

    edge_attr_dict_factory = single_edge_dict
G = ThinGraph()
G.add_edge(2, 1)
G[2][1]
{'weight': 1}
G.add_edge(2, 2)
G[2][1] is G[2][2]
True


#Barabasi_albert_graph
#RANDOM GRAPH
G = nx.barabasi_albert_graph(100,2)
nx.draw_spring(G)
plt.hist([v for k,v in nx.degree(G)])

plt.hist(nx.centrality.betweenness_centrality(G).values())

nx.diameter(G)

plt.show()

#Directed Graph

import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([("A", "B"), ("A", "C"), ("C", "B")])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="black")
nx.draw_networkx_labels(G, pos)
plt.show()