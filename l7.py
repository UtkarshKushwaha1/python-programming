#to print prime numbers b/w 1 to 100

for i in range (1,101):
    c=0
    for j in range (2,i):
        if(i%j)==0:c+=1
    if(c==0):
        print(i,end=' ')