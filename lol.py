#Write a program that reads some lines containing votes: each line contains a name.
#Have the program print the list of candidates in descending order of the number of votes received.

s="""modi 10
rahul 0
mamta 8
lalu 6
modi 8"""
m=0
r=0
ma=0
l=0
x=[]

for i in s.split("\n"):
        if 'modi' in i:
            m+=int(i[i.find(" ")+1:])
        if 'rahul' in i:
            r+=int(i[i.find(" ")+1:])
        if 'mamta' in i:
            ma+=int(i[i.find(" ")+1:])
        if 'lalu' in i:
            l+=int(i[i.find(" ")+1:])
    
d={m:'Modi',r:'Rahul',ma:'Mamta',l:'Lalu'}

for i in d.keys():
    x.append(i)

x.sort()

for i in x:
    print(d.get(i),":",i)