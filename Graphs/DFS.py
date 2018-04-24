from Graphs.adjacency_list import Graph
#from adjacency_list import Graph

stack = []
def dfs(g,v_list,value):
    stack.append(value)
    v_list[value] = True
    print(value)
    for k,v in g.edges[value].items():
        if not v_list[k]:
            stack.append(k)
            dfs(g,v_list,k)



def dfs_start(g,startIndex):
    visited  = [False]*len(g.get_graph())
    for i in range(len(visited)):
        if not visited[i]:
            dfs(g,visited,startIndex)




g = Graph()
for i in range(0, 6):
    g.add_vertices(i)
# add the edges
g.add_edge(0, 1,0)
g.add_edge(0, 2,0)
g.add_edge(1, 3,0)
g.add_edge(1, 4,0)
g.add_edge(2, 0,0)
g.add_edge(2, 4,0)
g.add_edge(3, 4,0)
g.add_edge(3, 5,0)
g.add_edge(4, 5,0)
g.add_edge(4, 2,0)
g.add_edge(4, 1,0)
g.add_edge(4, 3,0)
g.add_edge(5, 3,0)
g.add_edge(5, 4,0)

dfs_start(g,0)