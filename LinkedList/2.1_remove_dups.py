class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        if self.data:
            return self.data.__str__()
        else:
            return 'Empty Node'

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self):
        self.head = None

    def append_nodes(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def remove_dupls(self):
        unique_dict ={}
        node = self.head
        while node is not None:
            if node.data not in unique_dict.keys():
                unique_dict[node.data] = node
            else:
                if node.next:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                else:
                    node.prev.next = None

            node = node.next

    def print_list(self):

        node = self.head
        while node is not None:
            print ('{}'.format(node.data))
            node = node.next






ll = LinkedList()
ll.append_nodes(1)
ll.append_nodes(4)
ll.append_nodes(4)
ll.append_nodes(4)
ll.append_nodes(4)
print ('original list')
ll.print_list()
print ('*****************')
ll.remove_dupls()
print ('removed dupls list')
ll.print_list()