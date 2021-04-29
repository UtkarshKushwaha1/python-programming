#Find an element using list
try:
    x=[43,5,2,7,77,4,8,57,6,34,6,542,3]

    e=int(input("Enter vlaue:"))
    l=0
    
    for i in x:
        if i==e:
            l=+1

    if l==0:
        print("Element not found!")
    else:
        print("Element found at index",x.index(e),"!")
except:
    print("Wrong Input!!")
    print("Enter an integer value!!")

