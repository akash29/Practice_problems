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

    def get_len(self):
        node = self.head
        length = 0
        while node is not None:
            node = node.next
            length += 1
        return length

    def get_kth_last(self,k):
        length = self.get_len()
        if length > 0:
            start_ptr = self.head
            end_ptr = start_ptr
            if k <= length:
                for i in range(k):
                    if end_ptr.next:
                        end_ptr = end_ptr.next

                while end_ptr.next is not None:
                    start_ptr = start_ptr.next
                    end_ptr = end_ptr.next

                return start_ptr.data
            else:
                return 'k greater than length of list'
        else:
            return 'list is empty'



ll = LinkedList()
ll.append_nodes(1)
ll.append_nodes(2)
ll.append_nodes(3)
ll.append_nodes(4)
ll.append_nodes(7)
ll.append_nodes(9)
print (ll.head)
print(ll.get_kth_last(1))
print(ll.get_kth_last(3))
print(ll.get_kth_last(2))
print(ll.get_kth_last(6))