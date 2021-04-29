#WAP to print the counts of integer, float and strings in a given list.
x=[]
ch=None
inte=0
f=0
s=0
while(ch!='done'):
    n=input()
    x.append(n)
    print("more?")
    ch=input()

for i in x:
    try:
        int(i)
        inte+=1
    except:
        try:
            float(i)
            f+=1
        except:
            s+=1

print("Integers:",inte,"Float:",f,"Strings:",s)

