# Inverted Pyramid Pattern
n = int(input("Enter number of rows: "))

for i in range(n):
    # Print spaces
    print(" " * i, end="")
    # Print stars
    print("*" * (n - i))
