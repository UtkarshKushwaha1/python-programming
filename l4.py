#pattern
#     x 
#    x x
#   x x x
#  x x x x
x=int(input())

for l in range(1,x+1):
    print(" "*(x-l) + "x "*l)
    