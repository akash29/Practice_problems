class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{} -> {}'.format(self.data,self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def add_Node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

ll = LinkedList()
ll.add_Node(5)
ll.add_Node(6)

