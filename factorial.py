def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
print("factorial of 5 is: ",factorial(5))