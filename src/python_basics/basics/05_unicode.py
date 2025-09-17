def unicode_demo(text: str):
    """Print Unicode code point of each character and rebuild the string back."""
    codes = [ord(ch) for ch in text]  # Unicode values
    
    print("Character -> Unicode Code Point")
    for ch, code in zip(text, codes):
        print(f"{ch} -> U+{code:04X}")  # format like U+XXXX
    
    # Rebuild text from Unicode values
    rebuilt = ''.join(chr(code) for code in codes)
    print(f"\nReconstructed text from codes: {rebuilt}\n")


# Example usage
user_input = input("Enter some text (can include emojis 🌍😊 or other languages 你好): ")
unicode_demo(user_input)
