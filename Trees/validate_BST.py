class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def validate_bst(node, max_value=float('inf'), min_value=float('-inf')):
    if node is None:
        return True
    if node.data > max_value or node.data < min_value:
        return False
    else:
        return validate_bst(node.left, node.data, min_value) \
            and validate_bst(node.right, max_value, node.data)


n = Node(5)
n.left = Node(3)
n.left.left = Node(2)
n.left.right = Node(4)
n.right = Node(7)
n.right.left = Node(6)
n.right.right = Node(1)
print(validate_bst(n))
