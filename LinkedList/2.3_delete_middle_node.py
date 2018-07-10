class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.data,self.next)


class LinkedList:
    def __init__(self):
        self.head = None

    def appendNodes(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self,node):
        if node.next is not None or node.data != self.head.data:
            start_ptr = self.head
            prev_node = None
            while start_ptr != node:
                prev_node = start_ptr
                start_ptr = start_ptr.next

            prev_node.next = node.next
        else:
            print ("Node to be deleted is first or last")


ll = LinkedList()
ll.appendNodes(1)
ll.appendNodes(2)
ll.appendNodes(3)
ll.appendNodes(4)
ll.appendNodes(5)
print (ll.head)
k = 2
node = ll.head
for i in range(k):
    node = node.next
ll.delete_node(node)
print (ll.head)
