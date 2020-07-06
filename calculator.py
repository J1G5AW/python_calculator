#python 3.7.1

print(" ")
import time
print("this project was created by J1G5AW.\n(decimals can be used) ")
print(" ")
num1 = float(input("enter the first number : "))
operator = input("enter the operation(+ or - or × or ÷) : ")
num2 = float(input("enter the second number : "))
print(" ")
time.sleep(0.5)
if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "×":
  print(num1 * num2)
elif operator == "÷":
  print(num1 / num2)
else:
  print("Invalid operation! please choose from the given symbols.")
