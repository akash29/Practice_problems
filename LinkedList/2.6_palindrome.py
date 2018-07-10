from collections import deque
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

    def get_size(self):
        count = 0
        node = self.head
        while node:
            count+=1
            node = node.next

        return count

    def isPalindrome(self):
        front_stack = []
        back_stack = deque()
        slow_ptr = self.head
        fast_ptr = slow_ptr
        count = 0
        if self.get_size()>1:
            while fast_ptr and fast_ptr.next:
                front_stack.append(slow_ptr.data)
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
                count+=1
            middle_node = slow_ptr

            while middle_node:
                back_stack.append(middle_node.data)
                middle_node = middle_node.next


            while front_stack and back_stack:
                val_1 = front_stack.pop()
                val_2 = back_stack.popleft()
                if val_1 !=val_2:
                    return False

            if abs(len(front_stack)-len(back_stack))>1:
                return False

            return True
        else:
            return True

# use dict another impl
ll = LinkedList()
test_list = ['a','b']
for i in test_list:
    ll.append_node(i)

print(ll.isPalindrome())