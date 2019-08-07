class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

        def __repr__(self):
            return '{}->{}'.format(self.data,self.next)


def intersection_point(list1,list2):
    item_dict={}
    node_1 = list1
    node_2 = list2
    while node_1:
        item_dict[node_1.data] = node_1
        node_1 = node_1.next
    while node_2:
        if node_2.data in item_dict.keys():
            if item_dict[node_2.data]==node_2:
                return node_2.data
        node_2 = node_2.next
    else:
        return None





ll = LinkedList()
ll.head = ll.Node(1)
ll.head.next = ll.Node(2)
ll.head.next.next = ll.Node(3)
ll.head.next.next.next = ll.Node(4)

ll2 = LinkedList()
ll2.head = ll2.Node(6)
ll2.head.next = ll.head.next.next
ll2.head.next.next = ll.head.next.next.next

intersection_point(ll.head,ll2.head)