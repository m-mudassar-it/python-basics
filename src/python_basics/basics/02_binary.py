def to_binary(n: int) -> str:
    """Convert a non-negative integer to binary (base-2) representation."""
    if n < 0:
        raise ValueError("Binary conversion only supports non-negative integers")
    return bin(n)[2:]  # remove '0b' prefix


def from_binary(b: str) -> int:
    """Convert a binary (base-2) string back to integer."""
    if not all(ch in "01" for ch in b):
        raise ValueError("Binary string must only contain '0' and '1'")
    return int(b, 2)


# Example usage
print(f"to_binary(5): {to_binary(5)}")       # "101"
print(f"from_binary('101'): {from_binary('101')}") # 5
