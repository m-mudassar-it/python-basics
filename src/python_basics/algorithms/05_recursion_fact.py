def factorial(n: int, depth: int = 0) -> int:
    """Recursive factorial with logs showing each step."""
    indent = "  " * depth
    print(f"{indent}Enter factorial({n})")
    
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        print(f"{indent}Base case: factorial({n}) = 1")
        return 1

    sub = factorial(n - 1, depth + 1)      # recursive call (logs happen inside)
    result = n * sub
    print(f"{indent}Return factorial({n}) = {n} * {sub} = {result}")
    return result


# Example usage
num = 5
print(f"\nComputing factorial({num}):")
print(f"Result: factorial({num}) = {factorial(num)}")
