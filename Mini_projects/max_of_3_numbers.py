
def maxofnumber(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))

print("The maximun among the three number is : ", maxofnumber(x, y, z))