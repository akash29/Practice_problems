class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,data):
        self.stack.append(data)
        if len(self.min_stack)<1:
            self.min_stack.append(data)

        else:
            min_stack_val = self.min_stack[-1]
            min_val = min(data,min_stack_val)
            self.min_stack.append(min_val)

    def pop(self):
        if len(self.stack)>0 and len(self.min_stack)>0:
            val = self.stack.pop()
            self.min_stack.pop()
            return val
        else:
            raise Exception('stack is empty')

    def min(self):
        if len(self.min_stack)>0:
            min_val = self.min_stack[-1]
            return min_val
        else:
            return -1


s = Stack()
s.push(4)
s.push(5)
s.push(3)
s.push(7)
s.push(2)
print(s.min())
print("popped",s.pop())
print("popped",s.pop())
print("popped",s.pop())
print(s.min())
print("popped",s.pop())
print(s.min())
print("popped",s.pop())
print(s.min())