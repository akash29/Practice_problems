class Heap:
    def __init__(self, arr):
        self.arr = arr

    def heapify(self,i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left < len(self.arr) and self.arr[left] > self.arr[largest]:
            largest = left
        if right < len(self.arr) and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)

    def extract_top(self):
        max_value = self.arr[0]
        self.arr[0] = self. arr[-1]
        self.arr.pop()
        self.heapify(0)
        return max_value


test_arr=[12,5,787,1,23]
k = 2
heap = Heap(test_arr)
for i in range(len(test_arr)-1,-1,-1):
    heap.heapify(i)
for j in range(k):
    print(heap.extract_top())

