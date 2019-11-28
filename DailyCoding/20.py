class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return "{d1}->{d2}".format(d1=self.data,d2=self.next)
    

class Linkedlist(object):
    def __init__(self):
        self.head = None
        self.length = 0
    def add_nodes(self, node):
        node.next = self.head
        self.head = node
        self.length+=1


def find_intersection(l1,l2):
    m = l1.length
    n = l2.length
    bigger, smaller = (l1,l2) if m>n else (l2,l1)
    while  bigger is not None and bigger.length == smaller.length:
        temp = bigger.head
        bigger = temp.next
    while bigger is not None and smaller is not None:
        n1 = bigger.head.next
        n2 = smaller.head.next
        if n1==n2:
            return n1.data
        else:
            bigger = bigger.head.next
            smaller = smaller.head.next
    return None
    

l1 = Linkedlist()
l2 = Linkedlist()
node_list = [Node(i) for i in [10,8,7,3]]
for i in node_list:
    l1.add_nodes(i)
node_list_2 = node_list[:2]+[Node(i) for i in [1,99]]
for j in node_list_2:
    l2.add_nodes(j)

print(find_intersection(l1,l2))






