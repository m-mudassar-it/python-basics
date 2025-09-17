def merge_sort(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}Base case reached: {arr}")
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    print(f"{indent}Split into {left_half} and {right_half}")

    left_sorted = merge_sort(left_half, depth + 1)
    right_sorted = merge_sort(right_half, depth + 1)

    merged = merge(left_sorted, right_sorted, depth + 1)
    print(f"{indent}Merged {left_sorted} and {right_sorted} -> {merged}")
    return merged


def merge(left, right, depth=0):
    indent = "  " * depth
    print(f"{indent}Merging {left} and {right}")
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            print(f"{indent}Take {left[i]} from left")
            i += 1
        else:
            result.append(right[j])
            print(f"{indent}Take {right[j]} from right")
            j += 1

    # Append remaining elements
    while i < len(left):
        result.append(left[i])
        print(f"{indent}Take remaining {left[i]} from left")
        i += 1
    while j < len(right):
        result.append(right[j])
        print(f"{indent}Take remaining {right[j]} from right")
        j += 1

    print(f"{indent}Result of merge: {result}")
    return result


# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
print("\nStarting merge sort...\n")
sorted_numbers = merge_sort(numbers)
print(f"\n✅ Final sorted array: {sorted_numbers}")
