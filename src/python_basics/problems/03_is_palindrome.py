text = input("Enter a string: ")

# Normalize (remove spaces and make lowercase)
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome ✅")
else:
    print("Not a palindrome ❌")
