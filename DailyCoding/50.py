class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(node):
    if node.data.isnumeric():
        return float(node.data)
    
    return eval('{} {} {}'.format(in_order(node.left),node.data,in_order(node.right)))

n = Node('*')
n.left = Node('+')
n.right = Node('+')
n.left.left = Node('3')
n.left.right = Node('2')
n.right.left = Node('4')
n.right.right = Node('5')
print(in_order(n))