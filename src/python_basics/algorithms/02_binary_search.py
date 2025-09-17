def binary_search(arr, target):
    """Perform binary search with detailed logs."""
    left, right = 0, len(arr) - 1
    
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}:")
        print(f"   Current array slice: {arr[left:right+1]}")
        print(f"   Left index = {left}, Right index = {right}, Mid index = {mid}")
        print(f"   Middle element = {arr[mid]}")
        
        if arr[mid] == target:
            print(f"✅ Found {target} at index {mid}\n")
            return mid
        elif arr[mid] < target:
            print(f"➡️ {target} is greater than {arr[mid]}, moving right\n")
            left = mid + 1
        else:
            print(f"⬅️ {target} is smaller than {arr[mid]}, moving left\n")
            right = mid - 1
        step += 1
    
    print(f"❌ {target} not found\n")
    return -1


# Example usage
numbers = [2, 4, 5, 7, 8, 9, 11, 14, 18, 21]
target = 11

binary_search(numbers, target)
