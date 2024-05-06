#program to reverse a string without using any built-in functions
string = "Hello"
def reverseString(string):
    start = 0
    end = len(string) - 1
    string = list(string)
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    return "".join(string)
