class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def successor(node,val):
    suc = None
    while node:
        if node.data < val:
            node = node.right
        elif node.data > val:
            suc = node
            node = node.left
        else:
            suc_val = suc.data if suc else None
            return suc_val

node = Node(5)
node.left = Node(3)
node.left.left = Node(2)
node.left.right = Node(4)
node.right = Node(7)
print(successor(node,4))