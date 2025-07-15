def quick_sort_fruits(fruits, key='name'):
    # Base case
    if len(fruits) <= 1:
        return fruits
    
    # DIVIDE: Choose pivot and partition
    pivot, less_than, greater_than = partition_fruits(fruits, key)
    
    # CONQUER: Recursively sort partitions
    sorted_less = quick_sort_fruits(less_than, key)
    sorted_greater = quick_sort_fruits(greater_than, key)
    
    # COMBINE: Merge results
    return combine_partitions(sorted_less, pivot, sorted_greater)

def partition_fruits(fruits, key):
    """
    Divide step: partition fruits around a pivot
    
    Returns:
        tuple: (pivot_fruit, fruits_less_than_pivot, fruits_greater_than_pivot)
    """
    pivot = fruits[0]
    pivot_value = pivot[key]
    
    less_than = []
    greater_than = []
    
    for fruit in fruits[1:]:
        if fruit[key] < pivot_value:
            less_than.append(fruit)
        else:
            greater_than.append(fruit)
    
    return pivot, less_than, greater_than

def combine_partitions(sorted_less, pivot, sorted_greater):
    """
    Combine step: merge sorted partitions back together
    """
    return sorted_less + [pivot] + sorted_greater

# Usage example
def demonstrate_quicksort():
    sample_fruits = [
        {"name": "Mango", "price_per_lb": 3.99, "sweetness": 8},
        {"name": "Apple", "price_per_lb": 2.49, "sweetness": 6},
        {"name": "Banana", "price_per_lb": 1.29, "sweetness": 7},
        {"name": "Cherry", "price_per_lb": 5.99, "sweetness": 5}
    ]
    
    print("Original fruits:")
    for fruit in sample_fruits:
        print(f"  {fruit['name']}: ${fruit['price_per_lb']}")
    
    # Sort by price
    sorted_by_price = quick_sort_fruits(sample_fruits, 'price_per_lb')
    
    print("\nSorted by price:")
    for fruit in sorted_by_price:
        print(f"  {fruit['name']}: ${fruit['price_per_lb']}")
        

demonstrate_quicksort()