class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.data, self.next.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


def rotate(ll,node_val):
    head_node = ll.head
    p = head_node
    while p.next is not None:
        if p.data == node_val:
            break
        p = p.next
    new_head = p.next
    p.next = None
    r = new_head
    while r.next is not None:
        r = r.next
    r.next = head_node
    return new_head




ll = LinkedList()
ll.add_node('f')
ll.add_node('e')
ll.add_node('d')
ll.add_node('c')
ll.add_node('b')
ll.add_node('a')
new_ll = rotate(ll,'d')


