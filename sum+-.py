#WAP to print sum of all positive and negative numbers in a list.

x=[]
sp=0
sn=0
ch=None
print("Enter elemets in List:")
while(ch!="done"):
    n=int(input())
    x.append(n)
    print("Want to enter more?")
    ch=input()
    
for i in x:
    if(i>0):
        sp+=i
    if(i<0):
        sn+=i
print("Total negative numbers:",sn,"Total Positive Numbes:",sp)