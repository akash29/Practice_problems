from collections import deque

class QueueNode:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __repr__(self):
        return '{0}'.format(self.value)


def find_subarray(arr,sum):
    queue = deque()
    for i,j in enumerate(arr):
        node = QueueNode(i,j)
        sum -= node.value
        queue.append(node)

        while sum < 0:
            pop_node = queue.popleft()
            sum += pop_node.value
        if sum == 0:
            return queue
    return -1


test_arr = [1,2,3,7,5]
sum_req = 30
print(find_subarray(test_arr,sum_req))