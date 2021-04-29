try:
    x=[]
    c="a"
    coun=0
    while(c!="done"):
        a=int(input())
        x.append(a)
        coun+=1
        print("Done?")
        c=input()
    for i in x:
        print(i,end=" ")
    print("Total Number of element in List X are:",coun)
except:
    print("Invalid Input!")
    