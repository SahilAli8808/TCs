#program  to get smallest and second smallest element in an array

def smallestAndSecondSmallest(array):
    if len(array) < 2:
        return "Invalid Input"
    smallest = float('inf')
    second_smallest = float('inf')
    print("Smallest is: ", smallest, "Second smallest is: ", second_smallest)
    for i in range(len(array)):
        if array[i] < smallest:
            second_smallest = smallest
            smallest = array[i]
        elif array[i] < second_smallest and array[i] != smallest:
            second_smallest = array[i]
    if second_smallest == float('inf'):
        return "No second smallest element"
    return smallest, second_smallest

# Example usage:
arr = [5, 2, 7, 9, 3]
print("Smallest and second smallest elements are:", smallestAndSecondSmallest(arr))
arr = [5, 2]
print("Smallest and second smallest elements are:", smallestAndSecondSmallest(arr))

arr = [5, 2,1,1, 7, 9, 3]
print("Smallest and second smallest elements are:", smallestAndSecondSmallest(arr))