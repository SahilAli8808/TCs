def mean(array):
    return sum(array) / len(array)

def median(array):
    sorted_array = sorted(array)
    n = len(sorted_array)
    if n % 2 == 0:
        # If the length of the array is even, median is the average of the middle two elements
        return (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2
    else:
        # If the length of the array is odd, median is the middle element
        return sorted_array[n // 2]

# Input
array = list(map(int, input("Enter elements of the array separated by space: ").split()))

# Output
print("Mean:", mean(array))
print("Median:", median(array))
