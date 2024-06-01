"""
Alexander Perkins
For Sebastion Martell
Calculator
6/3/23
"""
import Calcumalator

num1 = ("")
num2 = ("")

print("Hello, and welcome to my calculator")
select = input("Would you want to multiply, add, subtract or divide: ")
if select.lower() == "multiply":
    num1 = input("What is the first number that you would like to multiply: ")
    num2 = input("What is the second number that you would like to multiply: ")
    product = (float(num1) * float(num2))
    if int(product) == float(num1) * float(num2):
        print(int(product))
    elif product == float(num1) * float(num2):
        print(product)
        
elif select.lower() == "add":
    num1 = input("What is the first number that you would like to add: ")
    num2 = input("What is the second number that you would like to add: ")
    product = (float(num1) + float(num2))
    if int(product) == float(num1) + float(num2):
        print(int(product))
    elif product == float(num1) + float(num2):
        print(product)
elif select.lower() == "subtract":
    num1 = input("What is the first number that you would like to subtract: ")
    num2 = input("What is the second number that you would like to subtract: ")
    product = (float(num1) - float(num2))
    if int(product) == float(num1) - float(num2):
        print(int(product))
    elif product == float(num1) - float(num2):
        print(product)
elif select.lower() == "divide":
    num1 = input("What is the first number that you would like to divide: ")
    num2 = input("What is the second number that you would like to divide: ")
    product = (float(num1) / float(num2))
    if int(product) == float(num1) / float(num2):
        print(int(product))
    elif product == float(num1) / float(num2):
        print(product)
else:
    print("not an answer,")
    exit = input("Would you like to restart?")
    if exit.lower() == "yes" or exit.lower() == "y":
        Calcumalator
    elif exit.lower() == "n" or exit.lower() == "no":
        print("Bye.")
        exit()
    