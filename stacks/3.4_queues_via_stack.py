class MyQueue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self,data):
        self.stack_1.append(data)

    def pop(self):
        while self.stack_1:
            val = self.stack_1.pop()
            self.stack_2.append(val)
        if self.stack_2:
            return self.stack_2.pop()
        else:
            return -1

    def peek(self):
        if len(self.stack_2)>0:
            return self.stack_2[0]


    def add_block(self, lists):
        for i in lists:
            self.push(i)

queue = MyQueue()
add_elem = [1,2,3,4,6,7]
queue.add_block(add_elem)
print(queue.pop())
print(queue.pop())
print(queue.pop())
queue.push(99)
print(queue.pop())
