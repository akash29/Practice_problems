
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return '{}->{}'.format(self.data, self.next)


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
        if r <self.size and self.arr[r].val < self.arr[smallest].val:
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
        if self.size >1 :
            self.build_heap()

    def k_merged_list(self,lists):
        for i in lists:
            self.add_element(i,i.data)

        out_list = LinkedList()
        while self.arr:
            min_obj = self.extract_min()
            min_node = min_obj.node
            min_val = min_obj.val
            out_list.insert_tail(min_val)
            if min_node.next:
                min_node = min_node.next
                min_val = min_node.data
                self.add_element(min_node,min_val)

        return out_list.head



    class Object:
        def __init__(self, node, val):
            self.node = node
            self.val = val



node = LinkedList()
node.insert_tail(1)
node.insert_tail(1)
node.insert_tail(2)
node.insert_tail(4)
node2 = LinkedList()
node2.insert_tail(1)
node2.insert_tail(2)
node2.insert_tail(3)
node2.insert_tail(4)
node3 = LinkedList()
node3.insert_tail(2)
node3.insert_tail(3)
node3.insert_tail(5)
lists = [node.head,node2.head,node3.head]
heap = Heap()
print(heap.k_merged_list(lists))
