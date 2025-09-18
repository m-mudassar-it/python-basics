# Fibonacci Series - Iterative

def fibonacci_iterative(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci_iterative(n))
