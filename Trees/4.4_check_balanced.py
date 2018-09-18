class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def check_height(self,node):
        if node is None:
            return 0

        left_tree = self.check_height(node.left)
        right_tree = self.check_height(node.right)
        return max(left_tree,right_tree)+1

    def isBalanced(self,node):
        if node is None:
            return True

        left_side = self.check_height(node.left)
        right_side = self.check_height(node.right)

        return abs(left_side-right_side)<=1 and self.isBalanced(node.left) and self.isBalanced(node.right)



tree_Node = Node(5)
tree_Node.left = Node(3)
tree_Node.right = Node(2)
tree_Node.left.left = Node(6)
tree_Node.left.right = Node(7)

print(tree_Node.isBalanced(tree_Node))