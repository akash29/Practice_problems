class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_height(node):
    if node is None:
        return 0
    left = check_height(node.left)
    right = check_height(node.right)
    return max(left, right) + 1


def isBalanced(node):
    if node is None:
        return True

    left_height = check_height(node.left)
    right_height = check_height(node.right)

    if abs(left_height - right_height) > 1:
        return False
    else:
        return isBalanced(node.left) and isBalanced(node.right)


def check_height_2(node):
    if node is None:
        return 0
    left = check_height_2(node.left)
    if left == float('-inf'):
        return float('-inf')
    right = check_height_2(node.right)
    if right == float('-inf'):
        return float('-inf')
    height = abs(left-right)
    if height > 1:
        return float('-inf')
    else:
        return max(left,right)+1


def isBalanced_2(node):
    return check_height_2(node) != float('-inf')


n = Node(4)
n.left = Node(2)
n.right = Node(6)
n.left.right = Node(3)
n.left.right.right = Node(8)
print(isBalanced(n))
print(isBalanced_2(n))