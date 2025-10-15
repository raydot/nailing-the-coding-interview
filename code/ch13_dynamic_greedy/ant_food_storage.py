def ant_food_storage_dp(storage_capacity, foods):
    # storage_capacity = total storage units available
    # foods = list of tuples (nutrition, storage_units, name)
    # Example: foods = [(4, 3, "Aphids"), (3, 2, "Larvae"), (2, 1, "Fungi")]
   
    memo = {}
    
    def dp(remaining_storage, food_index):
        # Base case
        if remaining_storage <= 0 or food_index >= len(foods):
            return 0, []
        
        # Have we already solved this subproblem?
        if (remaining_storage, food_index) in memo:
            return memo[(remaining_storage, food_index)]
        
        nutrition, storage_units, name = foods[food_index]
        
        # Option 1: Skip this food type entirely (move to next food type)
        skip_nutrition, skip_items = dp(remaining_storage, food_index + 1)
        
        # Option 2: Take one of this food type 
        take_nutrition = 0
        take_items = []
        if storage_units <= remaining_storage:
            # Take one item, then see what's optimal with remaining space
            remaining_nutrition, remaining_items = dp(remaining_storage - storage_units, food_index)
            take_nutrition = nutrition + remaining_nutrition
            take_items = [name] + remaining_items
        
        # Choose the option with maximum nutrition 
        if take_nutrition > skip_nutrition:
            best_option = (take_nutrition, take_items)
        else:
            best_option = (skip_nutrition, skip_items)
        
        # Memoize the result and return
        memo[(remaining_storage, food_index)] = best_option
        return best_option
    
    return dp(storage_capacity, 0)

def demonstrate_ant_storage(capacity=11):
    foods = [
        (9, 5, "Aphids"),   # 9 nutrition, 5 storage units
        (6, 4, "Larvae"),   # 6 nutrition, 4 storage units  
        (4, 3, "Fungi")     # 4 nutrition, 3 storage units
    ]
    
    storage_capacity = capacity
    
    print("=== Ant Food Storage Problem ===")
    print(f"Storage capacity: {storage_capacity} units")
    print("\nAvailable foods:")
    for nutrition, storage, name in foods:
        ratio = nutrition / storage
        print(f"  {name}: {nutrition} nutrition, {storage} storage (ratio: {ratio:.2f})")
        
    # Call the dynamic programming function
    max_nutrition, optimal_items = ant_food_storage_dp(storage_capacity, foods)
    
    
    print(f"\nOptimal solution: {max_nutrition} nutrition units")
    print("Selected items:")
    
    # Count and display the items
    from collections import Counter
    item_counts = Counter(optimal_items)
    
    total_storage_used = 0
    total_nutrition = 0
    
    for item_name, count in item_counts.items():
        # Find the nutrition and storage for this item
        for nutrition, storage, name in foods:
            if name == item_name:
                item_nutrition = nutrition * count
                item_storage = storage * count
                print(f"  {count} {item_name}: {item_nutrition} nutrition, {item_storage} storage")
                total_storage_used += item_storage
                total_nutrition += item_nutrition
                break
    
    print(f"\nTotal: {total_nutrition} nutrition, {total_storage_used} storage units used")
    print(f"Storage remaining: {storage_capacity - total_storage_used} units")

# Run the demonstration
demonstrate_ant_storage()