# === Functions in Python ===

# Example 1: Simple Function (no parameters, no return)
def greet():
    print("Hello, welcome to Python!")

print("=== Example 1: Simple Function ===")
greet()  # Calling the function
print()

# Example 2: Function with Parameters
def greet_person(name):
    print("Hello,", name)

print("=== Example 2: Function with Parameters ===")
greet_person("Alice")
greet_person("Bob")
print()


# Example 3: Function with Return Value
def add(a, b):
    return a + b

print("=== Example 3: Function with Return Value ===")
result = add(5, 3)
print(f"add(5, 3) = {result}")
print()


# Example 4: Function with Default Parameters
def power(base, exponent=2):
    return base ** exponent

print("=== Example 4: Function with Default Parameters ===")
print(f"power(5) = {power(5)} (default exponent=2)")
print(f"power(2, 3) = {power(2, 3)}")
print()


# Example 5: Function with Multiple Returns
def min_max(numbers):
    return min(numbers), max(numbers)

print("=== Example 5: Function with Multiple Returns ===")
nums = [3, 7, 2, 9, 5]
mn, mx = min_max(nums)
print(f"Numbers: {nums}, Min = {mn}, Max = {mx}")
print()


# Example 6: Built-in Functions
print("=== Example 6: Built-in Functions ===")
text = "Python"
print(f"len('{text}') = {len(text)}")
print(f"max([4, 7, 1, 9]) = {max([4, 7, 1, 9])}")
print(f"sum([1, 2, 3, 4]) = {sum([1, 2, 3, 4])}")
print()


# Example 7: Lambda Functions (anonymous functions)
print("=== Example 7: Lambda Functions ===")
square = lambda x: x * x
print(f"square(4) = {square(4)}")

add_nums = lambda a, b: a + b
print(f"add_nums(10, 20) = {add_nums(10, 20)}")

# Using lambda inside sorted() for custom sorting
words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
print(f"Words sorted by length: {sorted_words}")
print()


# Example 8: Nested Functions
def outer_function(msg):
    def inner_function():
        print("Inner function says:", msg)
    inner_function()

print("=== Example 8: Nested Functions ===")
outer_function("Hello from inner function!")
print()


# Example 9: Function with *args and **kwargs
def show_details(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print("=== Example 9: *args and **kwargs ===")
show_details(1, 2, 3, name="Alice", age=25)
print()


# === Summary ===
print("=== Summary ===")
print("1. Functions group reusable code into blocks.")
print("2. They can take inputs (parameters) and return outputs.")
print("3. Python supports built-in, user-defined, and lambda functions.")
print("4. Functions improve readability, reusability, and debugging.")
