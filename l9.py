#WAP to find pay commputation to give the employee  1.5 times the hourly rate for hours work above 40 hrs.


try:
    h=float(input("Input Hours:"))
    r=float(input("Input Rate:"))
    
    if(h>40):
        p=(h-40)*(1.5*r)+40*r
    else:
        p=h*r
    print(p)
except:
    print("ChecK input !")



