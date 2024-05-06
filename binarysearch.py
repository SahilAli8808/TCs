def binary_search(arr, target_element):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target_element:
            return mid
        elif arr[mid] < target_element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage:
print("element found at index: ",binary_search([1, 2, 3, 4, 5], 1))  # Output: 2