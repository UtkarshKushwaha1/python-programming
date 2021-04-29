#WAP to print counts of the numbers , sum and average
s=0
num=0
while(True):
    n=int(input())
    s+=n
    num+=1
    ch=input()
    if ch=="done":
        break
     

print("Total Numbers:",num,"Sum:",s,"Average:",s/num)