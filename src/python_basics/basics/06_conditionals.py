# === Conditionals in Python ===

print("=== Example 1: Simple if ===")
x = 10
if x > 5:
    print(f"{x} is greater than 5\n")


print("=== Example 2: if...else ===")
y = 3
if y % 2 == 0:
    print(f"{y} is Even\n")
else:
    print(f"{y} is Odd\n")


print("=== Example 3: if...elif...else ===")
marks = 72
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F")
print()


print("=== Example 4: Nested if ===")
age = 20
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You are allowed entry into the club.\n")
    else:
        print("You are NOT allowed entry into the club yet.\n")
else:
    print("You are a minor.\n")


print("=== Example 5: if inside a loop ===")
numbers = [5, 12, 7, 20, 3]
for n in numbers:
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")
