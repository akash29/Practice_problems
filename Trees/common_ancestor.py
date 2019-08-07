class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def DFS(node, find_node):
    visited = [False]*7
    path = []
    dfs_util(node, find_node, visited,path)


def dfs_util(node, find_n, visit, path):
    if node is None:
        return False
    visit[node.data] = True
    print(node.data)
    path.append(node.data)
    if node.data == find_n.data:
        return True

    if ((node.left is not None and dfs_util(node.left, find_n, visit,path)) or
            (node.right is not None and  dfs_util(node.right, find_n, visit,path))):
        return True

    path.pop()
    return False



n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.left.right = Node(5)
n.right = Node(3)
n.right.left = Node(6)
n.right.right = Node(7)
DFS(n,n.left.right)