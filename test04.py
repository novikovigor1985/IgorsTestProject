from colorama import init
from colorama import Fore, Back, Style

init()

print(Back.GREEN)

action = input("please select operation (+,-,*,/): ")
a = float(input("please first value: "))
b = float(input("please second value: "))
check = False

if action == "+":
    c = a + b
    
elif action == "-":
    c = a - b

elif action == "*":
    c = a * b
    
elif action == "/":
    c = a/b

else:
    print("Invalid operation");
    check = True

if not check:
    print(c)
    
input()