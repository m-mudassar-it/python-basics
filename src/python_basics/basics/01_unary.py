def to_unary(n: int) -> str:
    """Convert a non-negative integer to unary (base-1) representation."""
    if n < 0:
        raise ValueError("Unary system only supports non-negative integers")
    return "1" * n

def from_unary(u: str) -> int:
    """Convert a unary (base-1) string back to integer."""
    if not all(ch == "1" for ch in u):
        raise ValueError("Unary string must only contain '1'")
    return len(u)


# Example usage
print(f"to_unary(5): {to_unary(5)}")    # "11111"
print(f"from_unary('111'): {from_unary('111')}")  # 3
