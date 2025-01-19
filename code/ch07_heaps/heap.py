class MaxHeap:
    def __init__(self):
        self.items = []
        
    def get_left_child(self, index):
        return 2 * index + 1
        
    def get_right_child(self, index):
        return 2 * index + 2
        
    def delete_value(self, value):
        # Find value
        index = -1
        for i in range(len(self.items)):
            if self.items[i] == value:
                index = i
                break
                
        if index == -1:
            return None
            
        # Store value to return
        removed = self.items[index]
        
        # Replace with last element
        self.items[index] = self.items[-1]
        self.items.pop()
        
        # Bubble down if needed
        if index < len(self.items):
            self._bubble_down(index)
            
        return removed
        
    def _bubble_down(self, index):
        largest = index
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        
        if left < len(self.items) and self.items[left] > self.items[largest]:
            largest = left
            
        if right < len(self.items) and self.items[right] > self.items[largest]:
            largest = right
            
        if largest != index:
            self.items[index], self.items[largest] = self.items[largest], self.items[index]
            self._bubble_down(largest)
            
# Test MaxHeap
max_heap = MaxHeap()
initial_values = [50, 30, 20, 15, 10, 8, 16]

# Build heap
for value in initial_values:
    max_heap.items.append(value)

print("Initial heap:", max_heap.items)             # [50, 30, 20, 15, 10, 8, 16]
print("Removing 20:", max_heap.delete_value(20))   # 20
print("After removing 20:", max_heap.items)        # [50, 30, 16, 15, 10, 8]
print("Removing 50:", max_heap.delete_value(50))   # 50
print("After removing 50:", max_heap.items)   

# [30, 15, 16, 8, 10]