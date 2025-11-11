#Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#Returns the calculated factorial.
#Calls the function with a sample number and prints the output.

def factorial(a):
    if a==0 or a==1:
        return 1

    return a * factorial(a-1)

while True:

    number = input("Enter a number : ")
    if number.isdigit() and int(number)>0:
        print(f"The factorial of {number} is:",factorial(int(number)))
        break
    else:
        print("Invalid Input! Please try-again!")

"""
Factorial using Built-in function from MATH module
print(f"The factorial of the {number} is:",factorial(number))
"""
