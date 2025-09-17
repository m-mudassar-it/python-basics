def ascii_values_and_product(text: str):
    """Print ASCII values of each character and their multiplication."""
    values = [ord(ch) for ch in text]  # get ASCII value of each character
    
    print("Character -> ASCII Value")
    for ch, val in zip(text, values):
        print(f"{ch} -> {val}")
    
    product = 1
    for val in values:
        product *= val
    
    print(f"\nMultiplication of all ASCII values = {product}\n")


# Example usage
user_input = input("Enter some text: ")
ascii_values_and_product(user_input)
