import networkx as nx
import matplotlib.pyplot as plt

#G = nx.Graph()
#G.add_node(1)
#G.add_nodes_from([2,3])
#H = nx.path_graph(10)
#G.add_nodes_from(H)
#G.add_node(H)

#G.add_edge(1,2);
#e = (2,3)
#G.add_edge(*e)
#G.add_edges_from([(1,2), (1,3)])
#G.add_edges_from(H.edges())

G = nx.Graph(day="Friday")
G.graph
{'day': 'Friday'}
G.graph['day']='Monday'

G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
G.node[1]['room'] = 714
G.nodes(data=True)

G.add_edge(1, 2, weight=4.7)
G.add_edges_from([(3,4),(4,5)], color='red')
G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])

nx.draw(G);
plt.savefig("graph.png")