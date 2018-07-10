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

    def partition(self,val):
        start_node = self.head
        val_node = None
        prev_node = None
        while start_node is not None:
            if start_node.data < val:
                if val_node is None:
                    prev_node = start_node
                else:
                    prev_node.next = start_node.next
                    self.append_nodes(start_node.data)
            elif start_node.data == val:
                val_node = start_node
                prev_node = start_node
            else:
                prev_node = start_node

            start_node = start_node.next

        print(ll.head)


ll = LinkedList()
test1 = [1,2,10,5,8,5,0]
test2 = [0,1,2,3,4,5]
test3 = [10,9,8,7,6,5]
test4 = [5,6,7,8,9,10] # question days anywhere in right parition. if LL has all elem > than val then can it
                        # be anywhere in that list
for i in test1:
    ll.append_nodes(i)
print (ll.head)
ll.partition(5)