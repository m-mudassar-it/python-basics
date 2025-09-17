# ===== List Example =====
print("=== List Example ===")
my_list = [1, 2, 3]
print(f"Original list: {my_list}")

# Add element
my_list.append(4)
print(f"After append 4: {my_list}")

# Remove element
my_list.remove(2)
print(f"After remove 2: {my_list}")

# Access element
print(f"Element at index 1: {my_list[1]}")

# Iterate
print("Iterating over list:")
for item in my_list:
    print(item, end=" ")
print("\n")

# ===== Tuple Example =====
print("=== Tuple Example ===")
my_tuple = (10, 20, 30)
print(f"Original tuple: {my_tuple}")

# Access element
print(f"Element at index 0: {my_tuple[0]}")

# Tuple is immutable, so we cannot add/remove
# But we can concatenate to create a new tuple
new_tuple = my_tuple + (40,)
print(f"After concatenation: {new_tuple}")

# Iterating
print("Iterating over tuple:")
for item in new_tuple:
    print(item, end=" ")
print("\n")

# ===== Set Example =====
print("=== Set Example ===")
my_set = {1, 2, 3}
print(f"Original set: {my_set}")

# Add element
my_set.add(4)
print(f"After add 4: {my_set}")

# Remove element
my_set.discard(2)
print(f"After discard 2: {my_set}")

# Sets are unordered and unique
my_set.add(4)
print(f"After adding 4 again (no duplicates): {my_set}")

# Iterating
print("Iterating over set:")
for item in my_set:
    print(item, end=" ")
print("\n")

# ===== String Example =====
print("=== String Example ===")
my_string = "Hello World"
print(f"Original string: '{my_string}'")

# Access character
print(f"Character at index 0: '{my_string[0]}'")

# Substring
print(f"Substring (0-5): '{my_string[0:5]}'")

# String concatenation
new_string = my_string + "!!!"
print(f"After concatenation: '{new_string}'")

# Iterating over string
print("Iterating over string:")
for char in new_string:
    print(char, end=" ")
print()
