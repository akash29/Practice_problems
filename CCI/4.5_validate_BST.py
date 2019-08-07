class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def validate_BST(node, left_lim = float('-inf'), right_lim = float('inf')):
    if node is None:
        return True
    if node.data < left_lim or node.data > right_lim:
        return False
    return validate_BST(node.left,left_lim,node.data) and validate_BST(node.right,node.data,right_lim)

node = Node(5)
node.left = Node(3)
node.left.left = Node(2)
node.left.right = Node(4)
node.right = Node(7)
print(validate_BST(node))