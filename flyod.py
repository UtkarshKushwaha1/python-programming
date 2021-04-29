n=int(input())
l=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(l,end=" ")
        l+=1
    print()
    