class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert_nodes(arr, node):
    if len(arr) == 1:
        return Node(arr[0])
    else:
        middle_elem = len(arr)//2
        left_arr = arr[:middle_elem]
        node.left = insert_nodes(left_arr, node)
        right_arr = arr[middle_elem:]
        node.right = insert_nodes(right_arr, node.left)


def insert_node_util(arr):
    middle_elem = arr[len(arr)//2]
    node = Node(middle_elem)
    insert_nodes(arr, node)




test_arr = [1,2,3,4,5]
insert_node_util(test_arr)