class Stack:
    def __init__(self,threshold):
        self.stack = [0]*threshold

class SetofStacks:
    def __init__(self,threshold):
        self.stack = Stack(threshold)

    def get_new_stack(self):
        pass