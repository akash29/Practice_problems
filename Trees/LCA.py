class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def insert_nodes(data, side=None, parent=None):
    if parent is None:
        new_node = Node(data)
        return new_node
    else:
        new_node = Node(data)
        if side == 'left':
            parent.left = new_node
            new_node.parent = parent
        elif side == 'right':
            parent.right = new_node
            new_node.parent = parent
        return new_node


def get_depth(root, node, depth=0):
    if root is None:
        return 0
    if root.data == node.data:
        return depth
    d1 = get_depth(root.left, node, depth + 1)
    if d1 > 0:
        return d1
    d2 = get_depth(root.right, node, depth + 1)
    if d2>0:
        return d2
    return 0


def find_lca(root, node1, node2):
    depth1 = get_depth(root, node1)
    depth2 = get_depth(root, node2)
    diff_depth = 0
    larger_tree = None
    smaller_tree = None
    if depth1 > depth2:
        diff_depth = depth1-depth2
        larger_tree = node1
        smaller_tree = node2
    elif depth2 > depth1:
        diff_depth = depth2 - depth1
        larger_tree = node2
        smaller_tree = node1

    while diff_depth > 0:
        larger_tree = larger_tree.parent
        diff_depth -= 1

    while larger_tree is not None and smaller_tree is not None:
        if larger_tree == smaller_tree:
            return larger_tree.data

        larger_tree = larger_tree.parent
        smaller_tree = smaller_tree.parent

    return -1


n = insert_nodes(5)
n1 = insert_nodes(4,'left',n)
n2 = insert_nodes(3,'left',n1)
n3 = insert_nodes(2,'right',n2)
n4 = insert_nodes(8,'right',n)
n5 = insert_nodes(6,'left',n4)
print(find_lca(n,n2,n3))