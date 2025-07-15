def merge_sort_fruits(fruits, key='name'):
    """Sort fruits using merge sort algorithm"""
    # Base case
    if len(fruits) <= 1:
        return fruits
    
    # DIVIDE: Always split exactly in half
    mid = len(fruits) // 2
    left_half = merge_sort_fruits(fruits[:mid], key)
    right_half = merge_sort_fruits(fruits[mid:], key)
    
    # COMBINE: Merge the sorted halves
    return merge_sorted_halves(left_half, right_half, key)

def merge_sorted_halves(left, right, key):
    """
    Combine step: merge two sorted fruit lists into one sorted list
    
    Args:
        left: First sorted list of fruits
        right: Second sorted list of fruits
        key: The attribute to sort by
    
    Returns:
        Combined sorted list of fruits
    """
    merged_result = []
    i = j = 0
    
    # Compare first fruits from each sorted list and merge
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            merged_result.append(left[i])
            i += 1
        else:
            merged_result.append(right[j])
            j += 1
    
    # Add any remaining fruits from left list
    while i < len(left):
        merged_result.append(left[i])
        i += 1
    
    # Add any remaining fruits from right list
    while j < len(right):
        merged_result.append(right[j])
        j += 1
    
    return merged_result

# Usage example
def demonstrate_mergesort():
    """Demonstrate merge sort with sample fruit data"""
    sample_fruits = [
        {"name": "Mango", "price_per_lb": 3.99, "sweetness": 8},
        {"name": "Apple", "price_per_lb": 2.49, "sweetness": 6},
        {"name": "Banana", "price_per_lb": 1.29, "sweetness": 7},
        {"name": "Cherry", "price_per_lb": 5.99, "sweetness": 5}
    ]
    
    print("Original fruits:")
    for fruit in sample_fruits:
        print(f"  {fruit['name']}: ${fruit['price_per_lb']}")
    
    # Sort by price using merge sort
    sorted_by_price = merge_sort_fruits(sample_fruits, 'price_per_lb')
    
    print("\nSorted by price (merge sort):")
    for fruit in sorted_by_price:
        print(f"  {fruit['name']}: ${fruit['price_per_lb']}")

demonstrate_mergesort()