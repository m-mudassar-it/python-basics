# === Loops in Python ===

print("=== Example 1: For loop with list ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()


print("=== Example 2: For loop with range ===")
for i in range(1, 6):  # 1 to 5
    print(f"Number: {i}")
print()


print("=== Example 3: Nested for loops (multiplication table) ===")
for i in range(1, 4):   # rows
    for j in range(1, 4):   # columns
        print(f"{i} x {j} = {i*j}", end="  |  ")
    print()
print()


print("=== Example 4: While loop ===")
count = 1
while count <= 5:
    print(f"Count = {count}")
    count += 1
print()


print("=== Example 5: Break statement ===")
for i in range(1, 10):
    if i == 5:
        print("Breaking loop at 5")
        break
    print(i)
print()


print("=== Example 6: Continue statement ===")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
print()


print("=== Example 7: Pass statement ===")
for i in range(1, 4):
    if i == 2:
        pass  # placeholder, does nothing
        print("Pass executed (doing nothing)")
    print(i)
print()


print("=== Example 8: While loop with else ===")
n = 3
while n > 0:
    print(f"n = {n}")
    n -= 1
else:
    print("Loop ended naturally (no break)")
print()


print("=== Example 9: For loop with else ===")
for i in range(3):
    print(i)
else:
    print("For loop completed without break")
