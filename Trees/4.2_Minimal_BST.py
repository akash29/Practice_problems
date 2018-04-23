class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def construct_minimal_tree(arr):

    if not arr:
        return None

    middle = len(arr)//2

    root = Node(arr[middle])

    root.left = construct_minimal_tree(arr[:middle])
    root.right = construct_minimal_tree(arr[middle+1:])

    return root




def print_nodes(root):

    if root:
        print_nodes(root.left)
        print(root.data)
        print_nodes(root.right)

root_node= construct_minimal_tree([1,2,3,4,5,6,7,8])
print_nodes(root_node)

