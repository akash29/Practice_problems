class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postOrder(node, node_1,node_2):
    if not node:
        return None
    if node.data == node_1 or node.data==node_2:
        return node
    else:
        left = postOrder(node.left, node_1,node_2)
        right = postOrder(node.right,node_1,node_2)
        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right

tree = Tree(0)
tree.left = Tree(1)
tree.right = Tree(2)
tree.left.left = Tree(3)
tree.left.right = Tree(4)
tree.left.left.left = Tree(5)

node = postOrder(tree,5,4)
print("First common ancestor:", node.data)