def selection_sort(arr):
    """Selection sort with early stopping if no swap happens."""
    n = len(arr)
    print(f"Original array: {arr}\n")
    
    for i in range(n - 1):
        min_index = i
        
        # Find the index of the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # If min_index is the same, no swap is needed
        if min_index == i:
            print(f"Step {i+1}: No swap needed at index {i}, array already sorted!\n")
            break  # ✅ stop early
        else:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(f"Step {i+1}: Swap index {i} with min_index {min_index}")
            print(f"   Current array: {arr}\n")
    
    print(f"✅ Sorted array: {arr}")
    return arr


# Example usage
numbers1 = [11, 12, 22, 25, 64]  # Already sorted
numbers2 = [64, 25, 12, 22, 11]  # Unsorted

print("Case 1: Already sorted")
selection_sort(numbers1)

print("\nCase 2: Unsorted")
selection_sort(numbers2)
