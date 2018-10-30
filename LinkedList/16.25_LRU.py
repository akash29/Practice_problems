class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self,size):
        self.head = None
        self.tail = None
        self.size = size

    def add_node(self,k,v):
        if self.size > 0:
            node = Node(k,v)
            node.next = self.head
            node.prev = None
            if self.head is not None:
                self.head.prev = node
            self.head = node
            self.tail = self.head.next
            while self.tail is not None:
                if self.tail.next is None:
                    break
                else:
                    self.tail = self.tail.next
            self.size -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size += 1
            self.add_node(k,v)

    def __get_value_util(self, node, k):
        if node.key == k:
            temp_node = self.head
            node.prev.next = node.next
            self.head = node
            temp_node.prev = self.head
            self.head.next = temp_node
            self.head.prev = None
            self.tail = self.head.next
            while self.tail is not None:
                if self.tail.next is None:
                    break
                else:
                    self.tail = self.tail.next
            return self.head.value
        else:
            while node:
                node = node.next
                return self.__get_value_util(node, k)

    def get_value(self,k):
        node = self.head
        return self.__get_value_util(node,k)


l_list = LinkedList(4)
l_list.add_node(2,7)
l_list.add_node(4,4)
l_list.add_node(5,9)
l_list.add_node(6,10)
print(l_list.get_value(2))
l_list.add_node(11,12)
