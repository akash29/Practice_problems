class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.data,self.next)

def detect_loop(l_list):
    slow = l_list
    fast = l_list

    while l_list and fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


ll = LinkedList(1)
ll.next = LinkedList(2)
ll.next.next = LinkedList(4)
ll.next.next.next = LinkedList(6)
ll.next.next.next.next = ll

print(detect_loop(ll))