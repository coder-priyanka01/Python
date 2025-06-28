a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("good for you")

elif(a<0):
    print("You have entered an invalid age")

elif(a==0):
    print("You have entered 0 which is an invalid age")

else:
    print("You are below the age of consent")

print("This is the end of the program")

