a = int(input("Enter first number:"))
b = int(input("Enter second nunmber:"))

if(b ==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The Division a/b is {a/b}")