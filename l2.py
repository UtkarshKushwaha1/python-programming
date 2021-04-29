#Fibonacci Series
a,b = 0, 1
c = 0
 
while c <= 100:
    print(c, end = ' ')
    
    a = b
    b = c
    c = a + b
        