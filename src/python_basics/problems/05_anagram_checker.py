def is_anagram(str1, str2):
    # Remove spaces and make lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted letters are the same
    return sorted(str1) == sorted(str2)


# Example usage
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if is_anagram(word1, word2):
    print("✅ It's an Anagram")
else:
    print("❌ Not an Anagram")
