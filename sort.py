#BUBBLE SORTING

a=[3,13,5,4,6,45,68,34,23]
n=len(a)
for i in range(n):      
    for j in range(i, n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)
