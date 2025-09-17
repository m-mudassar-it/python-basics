def to_hexadecimal(n: int) -> str:
    """Convert integer to hexadecimal string with step logs."""
    if n < 0:
        raise ValueError("Only non-negative integers are supported")

    digits = "0123456789ABCDEF"
    steps = []
    original = n
    hex_str = ""

    # Repeated division method
    while n > 0:
        remainder = n % 16
        hex_str = digits[remainder] + hex_str
        steps.append(f"{n} ÷ 16 = {n//16} remainder {remainder} ({digits[remainder]})")
        n //= 16

    hex_str = hex_str if hex_str else "0"

    print(f"\nDecimal {original} -> Hexadecimal {hex_str}")
    print("Steps:")
    for s in steps:
        print("  " + s)
    return hex_str


def from_hexadecimal(h: str) -> int:
    """Convert hexadecimal string to integer with step logs."""
    h = h.upper()
    digits = "0123456789ABCDEF"
    value_map = {d: i for i, d in enumerate(digits)}

    result = 0
    power = len(h) - 1
    steps = []

    for ch in h:
        val = value_map[ch]
        steps.append(f"({16}^{power} * {ch}) = ({16}^{power} * {val}) = {val * (16**power)}")
        result += val * (16 ** power)
        power -= 1

    print(f"\nHexadecimal {h} -> Decimal {result}")
    print("Steps:")
    print("  " + " +\n  ".join(steps))
    return result


# Example usage
to_hexadecimal(255)
from_hexadecimal("FF")

to_hexadecimal(4095)
from_hexadecimal("1F4")
