
# Goal: ---- Build : a calculator that can do add, subtract, multiply, divide using functions.

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiple(x, y):
    return x*y
def divide(x, y):
    if y == 0:
        return "You cannot divide by zero."
    return x/y


print("Enter the choices : ")
print("1. Add 2. Subtraction 3. Multiplication 4. Division")

choice = int(input("Enter the choices 1   2   3  4 : "))

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

if choice == 1:
   print("Add : ", add(num1, num2))
elif choice == 2:
   print("Substraction : ", subtract(num1, num2))
elif choice == 3:
    print("Multiplication : ", multiple(num1, num2))
elif choice == 4:
   print("Division : ", divide(num1, num2))
else : print("Invalid choice.")


