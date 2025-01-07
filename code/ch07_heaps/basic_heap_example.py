class Heap:
    def __init__(self, input_list=None):
        self.heap = []
        if input_list:
            self.heap = input_list.copy()
    
    def get_parent(self, index):
        return (index - 1) // 2
    
    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, index):
        parent = self.get_parent(index)
        
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)
    
    def display(self):
        return self.heap

# Test the implementation
heap = Heap([75, 63, 60, 50, 15, 10, 5, 1])
print("Initial heap:", heap.display())
heap.insert(67)
print("After inserting 67:", heap.display())