class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self,k):
        i = 0
        current = self.head
        prev_node=None
        next_node = None
        while current is not None and i<k:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
            i+=1
        if next_node is not None:
            self.head.next = self.reverse(k)
        self.head = prev_node
        return prev_node



ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.add_node(6)
ll.reverse(3)
print(ll)
