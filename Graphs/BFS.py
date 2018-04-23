from adjacency_list import Graph
from collections import deque, defaultdict


def bfs(g, startIndex):
    visited = [False]*len(g.get_graph())
    d = deque()
    d.append(startIndex)
    visited[startIndex] = True
    predecessor = {startIndex:None}

    while d:
        leftElem = d.popleft()
        print (leftElem)

        edges = g.edges[leftElem]
        for k,v in edges.items():
            if not visited[k]:
                predecessor[k] = leftElem
                d.append(k)
                visited[k] = True

    print(predecessor)
    return predecessor

def find_predecessor(map, value):
    if map[value] is not None:
        pred = map[value]
        print(pred)
        find_predecessor(map,pred)


g = Graph()
for i in range(1, 6):
    g.add_vertices(i)
# add the edges
g.add_edge(0, 1,0)
g.add_edge(0, 2,0)
g.add_edge(1, 2,0)
g.add_edge(2, 0,0)
g.add_edge(2, 3,0)
g.add_edge(3, 3,0)
predecessor_map = bfs(g,2)
find_predecessor(predecessor_map,1)