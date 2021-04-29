# Write a program to perform calculator operation(+, *, /,%) in python.

o=input("Enter the operation for calculation (+,-, *, /,%):")

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))

if(o=='+'):
    print("Sum:",(x+y))
elif (o=='-'):
    print("Substraction:",(x-y))
elif (o=='/'):
    print("Division:",(x/y))
elif(o=='*'):
    print("Product:",(x*y))
elif(o=='%'):
    print("Modulus:",(x%y))
else:
    print('Wrong Input!!')


    