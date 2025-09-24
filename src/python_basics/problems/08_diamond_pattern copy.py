# Diamond Pattern
n = int(input("Enter number of rows: "))

# Upper half
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1))

# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1))
