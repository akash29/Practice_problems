from collections import defaultdict
class Heap:
    def __init__(self):
        self.array = []
        self.pos = []
        self.size = len(self.array)

    def minheapify(self,id):
        if self.size <0:
            return None
        left  = 2*id+1
        right = 2*id +2
        smallest = id
        if left <self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest != id:
            self.swapheap(smallest,id)
            self.minheapify(smallest)

    def swapheap(self,x1,x2):
        t = self.array[x1]
        self.array[x1] = self.array[x2]
        self.array[x2] = t

    def extractminheap(self):
        root = self.array[0]
        lastnode = self.array[self.size-1]
        self.array[0] = lastnode
        self.size -=1
        self.minheapify(0)
        return root

    def decreaseKey(self,key,value):
        self.array[key][1] = value
        while key > 0 and self.array[key][1] < self.array[int(key/2)][1]:
            self.swapheap(key,int(key/2))
            key = int(key/2)

class Graph:
    def __init__(self,v):
        self.v= v
        self.graph = defaultdict(list)

    def add_edges(self,src,dest,dist):
        self.graph[src].append([dest,dist])
        self.graph[dest].append([src,dist])

    def printArr(self,dist, n):
        print("Vertex\tDistance from source")
        for i in range(n):
            print("%d\t\t%d" % (i, dist[i]))

    def shortestDistance(self,src):
        distance = [float('inf')]*self.v
        distance[src] = 0
        heap = Heap()
        heap.size = self.v
        for i in range(self.v):
            heap.array.append([i,distance[i]])

        while heap.size > 0:
            u = heap.extractminheap()
            u_node = u[0]
            for v_node in self.graph[u_node]:
                v = v_node[0]

                if v < len(distance) and distance[u_node]!=float('inf') and distance[v] > distance[u_node] + v_node[1]:
                    distance[v] = distance[u_node] + v_node[1]

                    heap.decreaseKey(v,distance[v])

        print(distance)
        self.printArr(distance,self.v)


graph = Graph(9)
graph.add_edges(0, 1, 4)
graph.add_edges(0, 7, 8)
graph.add_edges(1, 2, 8)
graph.add_edges(1, 7, 11)
graph.add_edges(2, 3, 7)
graph.add_edges(2, 8, 2)
graph.add_edges(2, 5, 4)
graph.add_edges(3, 4, 9)
graph.add_edges(3, 5, 14)
graph.add_edges(4, 5, 10)
graph.add_edges(5, 6, 2)
graph.add_edges(6, 7, 1)
graph.add_edges(6, 8, 6)
graph.add_edges(7, 8, 7)
graph.shortestDistance(0)
