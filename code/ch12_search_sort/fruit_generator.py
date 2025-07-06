import random

def generate_fruit_data(num_fruits=100):
    """Generate a diverse database of fruits from around the world."""
    
    fruit_names = [
        # Common fruits
        "Apple", "Banana", "Orange", "Grape", "Strawberry", "Blueberry", "Raspberry",
        "Blackberry", "Cherry", "Peach", "Pear", "Plum", "Apricot", "Watermelon",
        "Cantaloupe", "Honeydew", "Pineapple", "Mango", "Papaya", "Kiwi",
        
        # Citrus varieties
        "Lemon", "Lime", "Grapefruit", "Tangerine", "Clementine", "Blood Orange",
        "Yuzu", "Bergamot", "Pomelo", "Key Lime",
        
        # Tropical fruits
        "Coconut", "Passion Fruit", "Dragon Fruit", "Star Fruit", "Guava",
        "Lychee", "Rambutan", "Durian", "Jackfruit", "Breadfruit", "Soursop",
        "Cherimoya", "Ackee", "Tamarind", "Plantain",
        
        # Berries and small fruits
        "Elderberry", "Gooseberry", "Currant", "Cranberry", "Lingonberry",
        "Cloudberry", "Mulberry", "Boysenberry", "Loganberry", "Huckleberry",
        
        # Stone fruits
        "Nectarine", "Damson", "Greengage", "Mirabelle", "Pluot", "Aprium",
        
        # Exotic and regional fruits
        "Persimmon", "Pomegranate", "Fig", "Date", "Olive", "Avocado",
        "Tomato", "Cucumber", "Eggplant", "Pepper", "Squash", "Pumpkin",
        "Acai", "Goji Berry", "Physalis", "Tomatillo", "Cactus Pear",
        "Horned Melon", "African Cucumber", "Buddha's Hand", "Finger Lime",
        
        # More exotic varieties
        "Salak", "Longan", "Langsat", "Mangosteen", "Rambai", "Pulasan",
        "Santol", "Mamey Sapote", "Sapodilla", "Sugar Apple", "Custard Apple",
        "Sweetsop", "Miracle Fruit", "Jabuticaba", "Pitanga", "Camu Camu",
        "Acerola", "Cashew Apple", "Marula", "Baobab Fruit", "Kei Apple",
        
        # Additional varieties to reach 100
        "Quince", "Medlar", "Serviceberry", "Pawpaw", "Maypop", "Muscadine",
        "Chokeberry", "Beautyberry", "Sumac Berry", "Rose Hip", "Hawthorn",
        "Sea Buckthorn", "Cornelian Cherry", "Jujube", "Loquat", "Feijoa"
    ]
    
    colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "White", "Black"]
    
    regions = [
        "North America", "South America", "Europe", "Asia", "Africa", 
        "Australia", "Mediterranean", "Caribbean", "Middle East", "Pacific Islands"
    ]
    
    textures = ["Smooth", "Fuzzy", "Bumpy", "Spiky", "Rough", "Waxy", "Soft", "Hard"]
    
    seasons = ["Spring", "Summer", "Fall", "Winter", "Year-round"]
    
    fruits = []
    for i in range(min(num_fruits, len(fruit_names))):
        fruit = {
            "id": i + 1,
            "name": fruit_names[i],
            "color": random.choice(colors),
            "region": random.choice(regions),
            "price_per_lb": round(random.uniform(0.99, 12.99), 2),  # $0.99 to $12.99
            "sweetness": random.randint(1, 10),  # 1-10 scale
            "texture": random.choice(textures),
            "season": random.choice(seasons),
            "vitamin_c": random.randint(5, 200),  # mg per 100g
            "size": random.choice(["Small", "Medium", "Large", "Extra Large"])
        }
        fruits.append(fruit)
    
    return fruits

# Usage
fruits = generate_fruit_data(100)
print(f"Generated {len(fruits)} fruits from around the world!")
print(fruits[:5])  # Print first 5 fruits for brevity

import hashlib

def hash_fruit(fruit):
    # Create a unique hash for each fruit based on its name
    return hashlib.sha256(fruit['name'].encode()).hexdigest()

def create_fruit_index(fruits):
    # Create a hash table to index fruits by their name
    fruit_index = {}
    for fruit in fruits:
        fruit_hash = hash_fruit(fruit)  # Generate a hash for the fruit 
        fruit_index[fruit_hash] = fruit  # Store the fruit in the index
    return fruit_index
  
# Example usage     
fruits = generate_fruit_data(100)
fruit_index = create_fruit_index(fruits)

# Print the index to verify
for fruit_hash, fruit in list(fruit_index.items())[:5]:  # Show first 5 entries
    print(f"Hash: {fruit_hash}, Fruit: {fruit}")

# Now you can search for a fruit by its hash
search_hash = hash_fruit({"name": "grape"})
if search_hash in fruit_index:
    print(f"Found fruit: {fruit_index[search_hash]}")
else:
    print("Fruit not found.")
    
    
import time

def search_without_index(fruits, search_term, search_type="name"):
    """Linear search through all fruits - O(n) time complexity"""
    results = []
    for fruit in fruits:
        if search_type == "name" and search_term.lower() in fruit['name'].lower():
            results.append(fruit)
        elif search_type == "color" and search_term.lower() == fruit['color'].lower():
            results.append(fruit)
        elif search_type == "region" and search_term.lower() == fruit['region'].lower():
            results.append(fruit)
    return results

def search_with_index(search_term, search_type, name_index, color_index, region_index):
    """Hash-based search using indexes - O(1) time complexity"""
    if search_type == "name":
        result = name_index.get(search_term.lower())
        return [result] if result else []
    elif search_type == "color":
        return color_index.get(search_term.lower(), [])
    elif search_type == "region":
        return region_index.get(search_term.lower(), [])
    return []
  
  
def create_searchable_fruit_index(fruits):
    """Create multiple indexes for different search types"""
    name_index = {}
    color_index = {}
    region_index = {}
    
    for fruit in fruits:
        # Index by name
        name_index[fruit['name'].lower()] = fruit
        
        # Index by color
        color = fruit['color'].lower()
        if color not in color_index:
            color_index[color] = []
        color_index[color].append(fruit)
        
        # Index by region
        region = fruit['region'].lower()
        if region not in region_index:
            region_index[region] = []
        region_index[region].append(fruit)
    
    return name_index, color_index, region_index

def demonstrate_search_performance():
    """Show the dramatic difference between indexed and non-indexed search"""
    
    # Generate test data
    fruits = generate_fruit_data(100)
    name_index, color_index, region_index = create_searchable_fruit_index(fruits)
    
    # Test searches
    test_searches = [
        ("Apple", "name"),
        ("Red", "color"),
        ("Asia", "region")
    ]
    
    print("Search Performance Comparison")
    print("=" * 50)
    
    for search_term, search_type in test_searches:
        print(f"\nSearching for {search_type}: '{search_term}'")
        
        # Linear search timing
        start_time = time.time()
        linear_results = search_without_index(fruits, search_term, search_type)
        linear_time = time.time() - start_time
        
        # Indexed search timing
        start_time = time.time()
        indexed_results = search_with_index(search_term, search_type, name_index, color_index, region_index)
        indexed_time = time.time() - start_time
        
        # Results
        print(f"  Linear search: {len(linear_results)} results in {linear_time:.6f} seconds")
        print(f"  Indexed search: {len(indexed_results)} results in {indexed_time:.6f} seconds")
        
        if indexed_time > 0:
            speedup = linear_time / indexed_time
            print(f"  Speed improvement: {speedup:.1f}x faster")
        else:
            print(f"  Speed improvement: Too fast to measure!")
            
if __name__ == "__main__":
    demonstrate_search_performance()