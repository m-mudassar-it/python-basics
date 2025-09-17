# === Libraries and Modules in Python ===

# --- Example 1: Importing Modules ---
import random           # import whole module
from random import randint, shuffle   # import specific functions

print("=== Example 1: Random Module ===")
print("Random number between 1 and 10:", random.randint(1, 10))
nums = [1, 2, 3, 4, 5]
shuffle(nums)
print("Shuffled list:", nums)
print()


# --- Example 2: Statistics Module ---
import statistics as stats

print("=== Example 2: Statistics Module ===")
data = [10, 20, 30, 40, 50]
print("Data:", data)
print("Mean:", stats.mean(data))
print("Median:", stats.median(data))
print("Standard Deviation:", stats.stdev(data))
print()


# --- Example 3: Using Packages (requests + PyPI) ---
# (You need to install requests: pip install requests)
import requests
import json

print("=== Example 3: Using Requests and JSON ===")
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)   # API call
if response.status_code == 200:
    data = response.json()  # Convert JSON response into dict
    print("API Response (dict):", data)
    print("Title:", data["title"])
    print("Completed:", data["completed"])
else:
    print("Failed to fetch API data")
print()


# --- Example 4: Custom Library (Custom Module) ---
# Let's assume we have a file named `mymath.py` with this code:
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
# Save it as `mymath.py` in the same directory.

print("=== Example 4: Custom Library ===")
import mymath   # importing custom module

print("Add(5, 3):", mymath.add(5, 3))
print("Multiply(4, 6):", mymath.multiply(4, 6))
print()


# --- Example 5: Summary ---
print("=== Summary ===")
print("1. Modules: Import built-in or external code.")
print("2. random: randint(), shuffle() for randomness.")
print("3. statistics: mean, median, stdev, etc.")
print("4. requests: Access APIs from the web (needs PyPI install).")
print("5. json: Parse API data easily.")
print("6. Custom libraries: Your own Python files used as modules.")
