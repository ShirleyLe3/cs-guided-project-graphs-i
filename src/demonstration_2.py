"""
4-color Theorom for World Maps
_______________________________________________________________________________
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).

You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).

The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.

*Note: We can color a graph in linear time and space. Also, make sure that your
solution can handle a loop in a reasonable way.*
"""
# Definition for a graph node.

"""
Go over all vertices:
    color each vertex based on colors allowed
    build legal colors
    find all of neighbors

    pick first legal/allowed color



    4-color theorem lookup
"""

# Definition for a graph node.


class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


​


def color_graph(graph, colors):
    # Go over all vertices
    for vertex in graph:
        # Color each vertex, based on whatever colors are legal
        # Build legal colors
        # Find all of our neighbors
        used_colors = set([neighbor.color for neighbor in vertex.neighbors])
        # pick the first legal color
        for color in colors:
            if color not in used_colors:
                vertex.color = color
                break


​
​
g1 = GraphNode('G1')
g2 = GraphNode('G2')
g3 = GraphNode('G3')
g4 = GraphNode('G4')
g5 = GraphNode('G5')
​
g1.neighbors.add(g2)
g1.neighbors.add(g4)
g1.neighbors.add(g3)
​
g2.neighbors.add(g1)
g2.neighbors.add(g4)
g2.neighbors.add(g5)
​
g3.neighbors.add(g1)
g3.neighbors.add(g5)
g3.neighbors.add(g4)
​
g4.neighbors.add(g1)
g4.neighbors.add(g2)
g4.neighbors.add(g3)
g4.neighbors.add(g5)
​
g5.neighbors.add(g2)
g5.neighbors.add(g3)
g5.neighbors.add(g4)
​
graph = [g1, g2, g3, g4, g5]
colors = set(['red', 'blue', 'green', 'orange', 'purple'])
​
color_graph(graph, colors)
​
for node in graph:
    print(node.color)
