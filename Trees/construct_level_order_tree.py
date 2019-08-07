class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def construct_tree(arr, i, root, n):
    if i < n:
        new_node = Node(arr[i])
        root = new_node
        root.left = construct_tree(arr, 2 * i + 1, root.left, n)
        root.right = construct_tree(arr, 2 * i + 2, root.right, n)

    return root


def preorder_construct(root):
    res_stack_1 = []
    res_stack_2 = []
    preorder_util_1(root, res_stack_1)
    preorder_util_2(root, res_stack_2)
    return res_stack_1,res_stack_2


def preorder_util_1(node, stack):
    if node is None:
        return
    stack.append(node.data)
    preorder_util_1(node.left, stack)
    preorder_util_1(node.right, stack)


def preorder_util_2(node, stack):
    if node is None:
        return
    stack.append(node.data)
    preorder_util_1(node.right, stack)
    preorder_util_1(node.left, stack)


temp_arr=[1,2,3,4]
root = None
start = 0
out = construct_tree(temp_arr, start, root, len(temp_arr))
print(preorder_construct(out))