# Scientific calculator in Python

import math

print("Welcome to the Scientific Calculator")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Logarithm")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

# Function to add two numbers
def add(x, y):
   return x + y

# Function to subtract two numbers
def subtract(x, y):
   return x - y

# Function to multiply two numbers
def multiply(x, y):
   return x * y

# Function to divide two numbers
def divide(x, y):
   return x / y

# Function to calculate exponentiation
def exponentiation(x, y):
   return x ** y

# Function to calculate logarithm
def logarithm(x):
   return math.log10(x)

# Function to calculate sine
def sine(x):
   return math.sin(x)

# Function to calculate cosine
def cosine(x):
   return math.cos(x)

# Function to calculate tangent
def tangent(x):
   return math.tan(x)

# Perform operation based on user's choice
if choice == '1':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   num1 = float(input("Enter base number: "))
   num2 = float(input("Enter exponent: "))
   print(num1,"^",num2,"=", exponentiation(num1,num2))

elif choice == '6':
   num1 = float(input("Enter number: "))
   print("log(",num1,") = ", logarithm(num1))

elif choice == '7':
   num1 = float(input("Enter angle in radians: "))
   print("sin(",num1,") = ", sine(num1))

elif choice == '8':
   num1 = float(input("Enter angle in radians: "))
   print("cos(",num1,") = ", cosine(num1))

elif choice == '9':
   num1 = float(input("Enter angle in radians: "))
   print("tan(",num1,") = ", tangent(num1))
   
else:
   print("Invalid input")
