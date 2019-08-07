class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}->{}'.format(self.data,self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node


def sum_lists_reverse(list1,list2):
    sum_list = LinkedList()
    carry = 0

    while list1 or list2:
        val1 = list1.data if list1 is not None else 0
        val2 = list2.data if list2 is not None else 0
        sum = val1+val2+carry
        carry = int(str(sum)[0]) if sum >9 else 0
        sum_list.insert_tail(sum%10)
        list1 = list1.next if list1 is not None else None
        list2 = list2.next if list2 is not None else None
    if carry > 0:
        sum_list.insert_tail(carry)
    return sum_list


def sum_lists_forward(list1,list2):
    stack_1,stack_2 = [],[]
    carry = 0
    sum_list = LinkedList()
    while list1:
        stack_1.append(list1.data)
        list1 = list1.next
    while list2:
        stack_2.append(list2.data)
        list2 = list2.next

    while stack_1 or stack_2:
        val1 = stack_1.pop() if len(stack_1)>0 else 0
        val2 = stack_2.pop() if len(stack_2)>0 else 0
        sum = val1+val2+carry
        carry = int(sum/10)
        sum_list.append_node(sum%10)

    if carry >0:
        sum_list.append_node(carry)

    return sum_list.head







ll_1 = LinkedList()
ll_2 = LinkedList()
test1 = [1,2,3]
test2 = [9,9]

for i in test1:
    ll_1.append_node(i)

for i in test2:
    ll_2.append_node(i)

res_list = sum_lists_reverse(ll_1.head,ll_2.head)
print (res_list.head)
print(sum_lists_forward(ll_1.head,ll_2.head))