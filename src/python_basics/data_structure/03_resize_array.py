def create_array(capacity=2):
    return [None] * capacity, 0   # (array, size)


def resize(array, new_capacity, size):
    new_arr = [None] * new_capacity
    for i in range(size):  # copy only actual elements
        new_arr[i] = array[i]
    print(f"Resized from capacity {len(array)} to {new_capacity}")
    return new_arr


def add(arr_tuple, item):
    array, size = arr_tuple
    if size == len(array):   # need to grow
        array = resize(array, 2 * len(array), size)
    array[size] = item
    size += 1
    print(f"Added {item} -> {array[:size]} (size={size}, capacity={len(array)})")
    return array, size


def remove(arr_tuple):
    array, size = arr_tuple
    if size == 0:
        print("Array is empty! Cannot remove.")
        return array, size
    
    removed = array[size - 1]
    array[size - 1] = None
    size -= 1
    print(f"Removed {removed} -> {array[:size]} (size={size}, capacity={len(array)})")
    
    # shrink if too empty
    if 0 < size <= len(array) // 4:
        array = resize(array, len(array) // 2, size)
    
    return array, size


# Example usage
arr, size = create_array(3)   # initial capacity = 3

arr, size = add((arr, size), 1)
arr, size = add((arr, size), 2)
arr, size = add((arr, size), 3)
arr, size = add((arr, size), 4)   # triggers resize

arr, size = remove((arr, size))
arr, size = remove((arr, size))
arr, size = remove((arr, size))   # should now shrink safely
