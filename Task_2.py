#Ask the user for a number as input.
#Use the math module to calculate the:
  #Square root of the number
  #Natural logarithm (log base e) of the number
  #Sine of the number (in radians)
import math


def operation(num:float):
    print("Square roor:",math.sqrt(num))
    print("Logarithm:",math.log(num))
    print("Sine:",math.sin(num))



while True:
    number = input("Enter a number : ")
    if number.isnumeric() and float(number)>=0:
        operation(float(number))
        break
    else:
        print("Invalid Input!. Input needs to be a positive numeric values.")
        print("Please Try-again!")
