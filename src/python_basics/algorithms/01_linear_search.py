def linear_search(arr, target):
    """Perform linear search on the list."""
    for index, value in enumerate(arr):    # enumerate(arr) gives pairs (index, value) for each element.
        if value == target:
            return index  # return position if found
    return -1  # return -1 if not found


# Example usage
numbers = [5, 3, 8, 4, 2, 9]
target = 4

result = linear_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
