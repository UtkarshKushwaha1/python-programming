# Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which take two parameters (hours and rate)
def computepay(n,m):
    if n>40:
        return (40*m)+(n-40)*(m*1.5)
    
    else:
        return n*m;

n=int(input("Enter hours:"))
m=int(input("Enter Rate:"))

print("Pay:",computepay(n,m))
    