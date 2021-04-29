#WAP to covert f to c or c to f using try and except block.

c=int(input("Enter 1 for F to C\nEnter 2 for C to F:"))

try: 
   
    if(c>2 or c<1): 1/0
    t=float(input())
    

    if(c==1):
        cel=(t-32)*(5/9)
        print("Temperature in C:",cel)
    else:
        f=(9/5)*t+32
        print("Temperature in F:",f)
except:
    print("Wrong Input!")

