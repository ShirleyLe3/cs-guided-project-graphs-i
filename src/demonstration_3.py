class Vertex:                           # Represent each vertex in graph
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight=0):
        # create connection with self, newvert, & set weight
        self.connections[vert] = weight

    def get_connections(self):          # retrieves all currently connected vertices
        return self.connections.keys()

    def get_value(self):                # retrieves value of vertex instance
        return self.value

    def get_weight(self, vert):         # get edge weight from vertex to spec vertex connected
        return self.connections[vert]


class Graph:                            # Map vertex names to spec vertex objects
    def __init__(self):
        self.vertices = {}
        self.count = 0                  # track #vertices. use dict

    def __contains__(self, vert):       # last step,                override methods
        return vert in self.vertices    # if vertex in vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight=0):   # create connection using fn
        if v1 not in self.vertices:         # check if in vertices,  ifnot add
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        # create connection bt 2 vertices, specify weight
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):                 # retrieve all vertices dict
        return self.vertices.keys()


# build graph structure in interactive environment
g = Graph()
for i in range(8):
    g.add_vertex(i)

g.add_edge(0, 1, 3)             # vertex 0 - 1     edgeWeight 3
g.add_edge(0, 7, 2)
g.add_edge(1, 3, 4)
g.add_edge(2, 2, 1)
g.add_edge(3, 6, 5)
g.add_edge(4, 0, 2)
g.add_edge(5, 2, 3)
g.add_edge(5, 3, 1)
g.add_edge(6, 2, 3)
g.add_edge(7, 1, 4)


# __________________________________________________________________________________
for v in g:
    for w in v.get_connections():
        print("( %s, %s )" % (v.get_value(), w.get_value()))

(0, 1)
(0, 7)
(1, 3)
(2, 2)
(3, 6)
(4, 0)
(5, 2)
(5, 3)
(6, 2)
(7, 1)

Vertex object at 0x7fd0f183f5e0
Vertex object at 0x7fd0f183fdc0
Vertex object at 0x7fd0f183fe20
Vertex object at 0x7fd0f183fb50
Vertex object at 0x7fd0f183fee0
Vertex object at 0x7fd0f183ff40
Vertex object at 0x7fd0f183ffd0
Vertex object at 0x7fd0f183ffa0
g.vertices
{0: < __main__.Vertex object at 0x7fd0f183f5e0 >, 1: < __main__.Vertex object at 0x7fd0f183fdc0 > , 2: < __main__.Vertex object at 0x7fd0f183fe20 > , 3: < __main__.Vertex object at 0x7fd0f183fb50 > , 4: < __main__.Vertex object at 0x7fd0f183fee0 > , 5: < __main__.Vertex object at 0x7fd0f183ff40 > , 6: < __main__.Vertex object at 0x7fd0f183ffd0 > , 7: < __main__.Vertex object at 0x7fd0f183ffa0 > }
