#Frequency
s="HELLO"
c=[]
for o in s:
    if o not in c:
        c.append(o)
for i in c:
    n=0
    for j in s:
        if i==j:
         n+=1
    print(i,":",n)