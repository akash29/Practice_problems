class Stacks:
    def __init__(self,num_stacks,capacity):
        self.top_stack = [-1]*num_stacks
        self.stack_data = [0]*capacity
        self.next_available = 0
        self.next_index = [i+1 for i in range(capacity)]
        self.next_index[capacity-1] = -1

    def push(self,stack_num,value):
        if stack_num < 0 or stack_num > len(self.top_stack):
            raise IndexError
        else:
            current_index = self.next_available
            self.next_available = self.next_index[current_index]
            self.stack_data[current_index] = value
            self.next_index[current_index] = self.top_stack[stack_num]
            self.top_stack[stack_num] = current_index

    def pop(self,stack_num):
        if stack_num < 0 or stack_num > len(self.top_stack):
            raise IndexError
        elif self.top_stack[stack_num] ==-1:
            raise Exception('stack is empty')
        else:
            current_index = self.top_stack[stack_num]
            value = self.stack_data[current_index]
            self.top_stack[stack_num] = self.next_index[current_index]
            self.next_index[current_index] = self.next_available
            self.next_available = current_index
            return value

stack = Stacks(3,9)
