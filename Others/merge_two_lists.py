class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.data,self.next)

def mergeList(l1,l2):

    current = dummy = LinkedList(0)
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next
    current.next = l1 or l2

    return dummy.next




list_1 = LinkedList(1)
list_1.next = LinkedList(3)
list_1.next.next = LinkedList(5)

list_2 = LinkedList(2)
list_2.next = LinkedList(6)
list_2.next.next = LinkedList(7)

mergeList(list_1,list_2)