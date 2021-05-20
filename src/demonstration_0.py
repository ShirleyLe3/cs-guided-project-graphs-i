"""
Graphs



Purpose

Uses:
Advantages:
Disadvantages:

"""
#                           GRAPH MATRIX
# ________________________________________________________________________________________________________
# class Graph:
#     def __init__(self)


graph = [
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
]
# Matrix must be square
# get second vertex and its edges
second_vertex = graph[1]

# Find out if third and last vertex connected
print(graph[2][4] == 1)

# Make new connection from B to E
graph[1][4] = 1


# ________________________________________________________________________________________________________

#                           GRAPH LIST
# ________________________________________________________________________________________________________
# single argument, & array that will set

graph = {
    'a': set(['b', 'c', 'd']),
    'b': set(),
    'c': set(['e']),
    'd': set(['e']),
    'e': set(['a']),        # connects E to A
}
