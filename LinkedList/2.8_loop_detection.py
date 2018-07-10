class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.data,self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def append_nodes(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_circular_node(self):
        item_dict={}
        node = self.head
        while node:
            if node.data not in item_dict.keys():
                item_dict[node.data] = node
                node = node.next
            else:
                return node.data
        return None

ll = LinkedList()
test = ['c','e','d','c','b','a']
for i in test:
    ll.append_nodes(i)
print(ll.get_circular_node())