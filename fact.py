# Factorial of a number

def fact(n):
    f=1
    for i in range(n,1,-1):
        f*=i;
    return f;

#main  
x=int(input("Enter a number:"))
print("Its factorial:",fact(x))