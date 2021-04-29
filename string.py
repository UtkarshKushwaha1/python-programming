#Program to count number of words in a string

s=input("Enter string:")

i=0
c=1
if len(s)>0:
    for i in s:
        if i==' ':
            c+=1
elif len(s)==0:
    c=0

print("Total number of words:",c)
