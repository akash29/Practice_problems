class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.data,self.next)

    class LinkedList:
        def __init__(self):
            self.head = None

        def insert_tail(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node




class Heap:
    def __init__(self):
        self.size = 0
        self.arr = []

    def heapify(self, root):
        l = root*2+1
        r = root*2+2
        smallest = root
        if l < self.size and self.arr[l].val < self.arr[root].val:
            smallest = l
        if r <self.size and self.arr[smallest].val < self.arr[r].val:
            smallest = r
        if smallest != root:
            self.arr[smallest],self.arr[root] = self.arr[root], self.arr[smallest]
            self.heapify(smallest)

    def build_heap(self):
        for i in range(self.size//2,-1,-1):
            self.heapify(i)

    def extract_min(self):
        min_val = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.arr.pop()
        self.size-=1
        self.heapify(0)
        return min_val

    def add_element(self,node,val):
        new_object = self.Object(node,val)
        self.arr.append(new_object)
        self.size+=1
        self.build_heap()

    class Object:
        def __init__(self, node, val):
            self.node = node
            self.val = val

def k_merge_lists(lists):
    pass


node = Node.LinkedList()
node.insert_tail(1)
node.insert_tail(1)
node.insert_tail(2)
node.insert_tail(4)
node2 = Node.LinkedList()
node2.insert_tail(1)
node2.insert_tail(2)
node2.insert_tail(3)
node2.insert_tail(4)
node3 = Node.LinkedList()
node3.insert_tail(2)
node3.insert_tail(3)
node3.insert_tail(5)
lists = [node,node2,node3]
