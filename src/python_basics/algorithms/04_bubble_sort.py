def bubble_sort(arr):
    """Bubble sort with proper early stopping and logs."""
    n = len(arr)
    print(f"Original array: {arr}\n")

    for i in range(n - 1):
        swapped = False
        print(f"Pass {i+1}:")
        
        for j in range(n - 1 - i):
            print(f"   Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"   Swapped -> {arr}")
            else:
                print(f"   No swap -> {arr}")

        if not swapped:
            print(f"✅ No swaps in pass {i+1}, array is sorted early!\n")
            break  # ✅ stop immediately when no swaps happen
        else:
            print(f"Array after pass {i+1}: {arr}\n")

    print(f"✅ Sorted array: {arr}")
    return arr


# Example usage
print("Case 1: Already sorted")
bubble_sort([1, 2, 3, 4, 5])

print("\nCase 2: Unsorted")
bubble_sort([64, 34, 25, 12, 22, 11, 90])
