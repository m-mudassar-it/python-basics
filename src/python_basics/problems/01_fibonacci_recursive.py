# Fibonacci Series - Recursive

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", [fibonacci_recursive(i) for i in range(n)])
