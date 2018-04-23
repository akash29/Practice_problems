def BuildAdjacencyList(a):
    graph = {}
    # create nodes
    for word in a:
        for c in word:
            if c not in graph.keys():
                graph[c] = []
    # create edges
    size = len(graph)
    for i in range(0, size):
        w1 = a[i][0]
        if (i + 1 < size):
            w2 = a[i + 1][0]
        else:
            w2 = ""
        if (w1 != w2 and len(w2) > 0):
            graph[w1].append(w2)
    # for key in graph:
    #	print(key,graph[key])
    return graph

BuildAdjacencyList(["baa", "abcd", "abca", "cab", "cad"])
