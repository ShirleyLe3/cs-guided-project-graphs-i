

graph = {
    'a': set(['b', 'c', 'd']),
    'b': set(),
    'c': set(['e']),
    'd': set(['e']),
    'e': set(['a']),        # connects E to A
}

# Find out paths A connect to E
# ________________________________________________________________________________________________________

#                           PATH BETWEEN VERTICES
# # ________________________________________________________________________________________________________
#

all_paths = []


def print_graph(current_vertex, path):
    print(current_vertex)
    # Recurse on the children
    new_path = path + [current_vertex]
    # I have reached the end of my path because the neighbor is empty
    if len(graph[current_vertex]) == 0:
        all_paths.append(new_path)


​
   for neighbor in graph[current_vertex]:
        # print ['a'. 'c', 'e'], ['a'. 'b'], ['a'. 'd', 'e'],
        print_graph(neighbor, new_path.copy())
    ​
​


print_graph('c')
print_graph('a', [])
print(all_paths)


def print_tree_pre_order(root):
    print(root.value)

    if root.left:                     # if can go left
        print_tree_pre_order(root.left)  # recurse left
    if root.right:
        print_tree_pre_order(root.right)

        # two ways to get to E,    a-c-e,    a-d-e







"""
                                                UNDERSTAND
generate all possible solutions using depth-first seaerch      &  backtracking

inititialize visited array false, currPath,  simplePath
depth-first search for ll simple paths
check vertrx u visited & add to currPath
check u = v     reached destination
check other neighbors (recursively) for path
remove u from currPath   &  mark u unvisited


_______________________________________________________________________________________________________________________
                                                PLAN

DATA  graph stored in adjacency list
        Starting node
        ending node

RESULT  
        visited -- (false)
        currentPath --{}            will store curPath
        simplePaths --{}            store resulting paths
        DFS(u, v)                   return resulting simplePaths depth-first-search
        return simplPaths           return list of all simplePath from u  - v

FUNCTION
    if visited(u) = true            *check vertex visted
        return                      add path to list
    end
    visited(u) -- true
    currentPath.addToBack(u)
    if u = v then                   *check if vertex u  equal destination v
        simplePath.add(currentPath)
        visited(u) -- false
        currentPath.removeFromBack()    *lastly, removes value stored. mark node 'unvisited' to recheck path 
        return
    end
    for next                        *check path recursively for neughbor of currvertex
        DFS(next, v)    
    end
    currentPath.removeFromBack()
    visited(u) --false 
end       
        
"""
