# === Exception Handling in Python ===

print("=== Example 1: Basic try-except ===")
try:
    num = int("abc")   # this will raise ValueError
    print("Number:", num)
except ValueError:
    print("Error: Cannot convert string to integer")
print()


print("=== Example 2: Handling multiple exceptions ===")
try:
    result = 10 / 0   # ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid value")
print()


print("=== Example 3: Using else block ===")
try:
    num = int("100")
except ValueError:
    print("Error: Invalid conversion")
else:
    print("Conversion successful, num =", num)
print()


print("=== Example 4: Using finally block ===")
try:
    file = open("test.txt", "w")
    file.write("Hello, World!")
except IOError:
    print("Error: File operation failed")
finally:
    file.close()
    print("File closed (finally block executed)")
print()


print("=== Example 5: Catching multiple exceptions together ===")
try:
    nums = [1, 2, 3]
    print(nums[5])  # IndexError
except (IndexError, ValueError) as e:
    print("Caught exception:", e)
print()


print("=== Example 6: Raising exceptions manually ===")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age is valid:", age)

try:
    check_age(-5)
except ValueError as e:
    print("Exception raised:", e)
print()


print("=== Example 7: Custom exceptions ===")
class MyCustomError(Exception):
    pass

def risky_function(x):
    if x == 0:
        raise MyCustomError("Custom error: x cannot be zero")
    return 10 / x

try:
    risky_function(0)
except MyCustomError as e:
    print("Caught custom exception:", e)
print()


print("=== Example 8: Try-Except inside a loop ===")
nums = [10, 0, 5, "abc", 2]
for n in nums:
    try:
        print(f"10 / {n} = {10 / int(n)}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error with {n}: {e}")
print()


print("=== Summary ===")
print("1. try-except prevents program crash.")
print("2. else runs if no exception occurs.")
print("3. finally always runs (cleanup).")
print("4. You can raise and define custom exceptions.")
