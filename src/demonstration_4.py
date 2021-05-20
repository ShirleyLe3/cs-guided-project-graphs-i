class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight=0):
        self.connections[vert] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def get_vertices(self):
        return self.vertices.keys()


g = Graph()

g.add_vertex("A")
Vertex object at 0x7fd1a4c68ac0
g.add_vertex("B")
Vertex object at 0x7fd1a4c68ac0
g.add_vertex("C")
Vertex object at 0x7fd1a4c68ac0
g.add_vertex("D")
Vertex object at 0x7fd1a4c68ac0
g.add_vertex("E")
Vertex object at 0x7fd1a4c68ac0
g.add_edge(A, B, 1)
g.add_edge(B, C, 3)
g.add_edge(B, D, 2)
g.add_edge(E, D, 1)
