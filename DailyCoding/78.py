class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

def heapify(arr,i ,n):
    smallest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left].data <= arr[smallest].data:
        smallest = left
    if right < n and arr[right].data <= arr[smallest].data:
        smallest = right
    
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, smallest, n)

def extract_min(arr, res_ll):
    n = len(arr)
    if n > 0:
        val = arr[0]
        arr[0] = arr[-1]
        arr.pop()
        res_ll.add_node(val.data)
        heapify(arr,0,n-1)
        while arr:
            extract_min(arr,res_ll)
    else:
        return


def initialize_ll(*arr):
    out_arr = []
    for ar in arr[0]:
        l = LinkedList()
        for i in ar:
            l.add_node(i)
        out_arr.append(l)
    return out_arr



sorted_arrs = [[1,3,5],[2,3,4,6],[0,7]]
ll_list = initialize_ll(sorted_arrs)
new_list = []
while ll_list:
    val = ll_list.pop()
    new_list.append(val.head)

n = len(new_list)
for i in range(n-1,-1,-1):
    heapify(new_list,i,n)
out_ll = LinkedList()
extract_min(new_list,out_ll)








