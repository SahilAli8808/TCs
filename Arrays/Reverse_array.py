#Python program to reverse an array without using any built-in functions
arraylist = [1,2,3,4,5,6]
def reverseArray(arraylist):
    start = 0
    end = len(arraylist) - 1
    # print("End is: ", end)
    while start < end:
        arraylist[start], arraylist[end] = arraylist[end], arraylist[start]
        start += 1
        end -= 1
    return arraylist



print("Original array is: ", arraylist)
print("Reversed array is: ", reverseArray(arraylist))   