# queue using 2 stack

class Queue(object):
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    def enqueue(self, elem):
        self.stack_1.append(elem)
    def dequeue(self):
        if not self.stack_2:
            while self.stack_1:
                elem = self.stack_1.pop()
                self.stack_2.append(elem)
        if self.stack_2:
            return self.stack_2.pop()
        else:
            return None

q = Queue()
q.enqueue(34)
q.enqueue(-50)
q.enqueue(42)
print(q.dequeue())
q.enqueue(1)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())