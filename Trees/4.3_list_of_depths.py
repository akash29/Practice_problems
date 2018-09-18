from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.data,self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_depth(node):
    bfs_queue = deque()
    bfs_queue.append(node)
    bfs_queue.append(None)
    ll_list = []
    temp_list = []
    depth=0
    while bfs_queue:
        node = bfs_queue.popleft()
        if node is None:
            depth+=1
            bfs_queue.append(None)
            if bfs_queue[0] is None:
                break
            print ("depth", depth)
        if node is not None and node.left is not None:
            bfs_queue.append(node.left)
        if node is not None and node.right is not None:
            bfs_queue.append(node.right)
    return ll_list



tree = Tree(1)
tree.left = Tree(2)
tree.right = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
print(find_depth(tree))


