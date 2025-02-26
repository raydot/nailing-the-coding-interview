import random

def heapify(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            parent = (i - 1) // 2
            if arr[i] > arr[parent]:
                arr[i], arr[parent] = arr[parent], arr[i]
                swapped = True
    return arr
  
# Test the function
def is_max_heap(arr):
    for i in range(1, len(arr)):
        parent = (i - 1) // 2
        if arr[i] > arr[parent]:
            return False
    return True
  

random_array = [random.randint(1, 100) for _ in range(10)]
print(random_array)

heapified_array = heapify(random_array)
print(heapified_array)
print(is_max_heap(heapified_array))