#this is for sorted linkedlists

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def get_len(linked_lst):
    temp = linked_lst.head
    count = 0
    while temp:
        count+=1
        temp = temp.next
    return count

def get_intersection(head1,head2,result_head):
    while head1 and head2:
        if head1.data>head2.data:
            head2 = head2.next
        elif head2.data > head1.data:
            head1 = head1.next
        else:
            result_head.add_node(head1.data)
            head1 = head1.next
            head2 = head2.next


    return result_head


ll1 = LinkedList()
ll2 = LinkedList()
ll1.add_node(6)
ll1.add_node(5)
ll1.add_node(4)
ll1.add_node(2)
ll1.add_node(1)
ll2.add_node(8)
ll2.add_node(4)
ll2.add_node(3)
ll2.add_node(2)
result_list = LinkedList()
n1= get_len(ll1)
n2 = get_len(ll2)
get_intersection(ll1.head,ll2.head,result_list)


