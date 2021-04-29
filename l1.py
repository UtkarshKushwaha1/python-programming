#Perfect square
import math
x=int(input())

s=math.sqrt(x)

print(s)

if(x%s==0):
    print("perfect square")
else:
    print("not a perfect square!")
    