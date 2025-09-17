# Simple Dictionary Implementation

# Initialize hash table
SIZE = 5
hash_table = [[] for _ in range(SIZE)]  # list of empty buckets
# Example after initialization: hash_table = [[], [], [], [], []]


# Simple hash function
def hash_key(key):
    print(f"Hashing key '{key}'")
    return hash(key) % SIZE

# Insert key-value pair
def insert(key, value):
    index = hash_key(key)
    # Check if key already exists, update
    for i, (k, v) in enumerate(hash_table[index]):
        if k == key:
            hash_table[index][i] = (key, value)
            print(f"Updated key '{key}' with value '{value}' in bucket {index}")
            return
    # If key not found, append
    hash_table[index].append((key, value))
    print(f"Inserted key '{key}' with value '{value}' in bucket {index}")

# Get value by key
def get(key):
    index = hash_key(key)
    for k, v in hash_table[index]:
        if k == key:
            print(f"Found key '{key}' with value '{v}' in bucket {index}")
            return v
    print(f"Key '{key}' not found")
    return None

# Remove key-value pair
def remove(key):
    index = hash_key(key)
    for i, (k, v) in enumerate(hash_table[index]):
        if k == key:
            del hash_table[index][i]
            print(f"Removed key '{key}' from bucket {index}")
            return
    print(f"Key '{key}' not found for removal")

# Print entire dictionary
def display():
    print("\nCurrent Dictionary:")
    for i, bucket in enumerate(hash_table):
        print(f"Bucket {i}: {bucket}")

# Example usage
insert("apple", 10)
insert("banana", 20)
insert("orange", 30)
insert("grape", 40)
insert("apple", 50)   # update existing key
insert("pineapple", 60)
insert("pear", 70)
insert("mango", 80)
insert("strawberry", 90)
insert("watermelon", 100)
insert("kiwi", 110)
display()
get("banana")
remove("orange")
display()
get("orange")
