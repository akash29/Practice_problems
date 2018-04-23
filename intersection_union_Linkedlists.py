class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_Node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def findIntersection(list1,list2):
    elem_map = {}
    head1 = list1.head
    head2 = list2.head
    common_elem = []
    while head1:
        data_val = head1.data
        elem_map[data_val] = head1
        head1 = head1.next
    while head2:
        data_val = head2.data
        if data_val in elem_map:
            common_elem.append(data_val)
        head2 = head2.next

    return common_elem

def findUnion(list1,list2):
    elem_map = {}
    head1 = list1.head
    head2 = list2.head
    union_elem = []
    while head1:
        elem_map[head1.data] = head1
        if head1.data not in union_elem:
            union_elem.append(head1.data)
        head1 = head1.next
    while head2:
        data_val = head2.data
        if data_val not in elem_map:
            union_elem.append(data_val)
        head2 = head2.next

    return union_elem


ll1 = LinkedList()
ll2 = LinkedList()
ll1.add_Node(6)
ll1.add_Node(5)
ll1.add_Node(4)
ll1.add_Node(2)
ll1.add_Node(1)
ll2.add_Node(8)
ll2.add_Node(4)
ll2.add_Node(3)
ll2.add_Node(2)
print(findIntersection(ll1,ll2))
print(findUnion(ll1,ll2))