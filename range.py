
# Use of list
"""
smallest  = None
for i in [4,5,3,6,2]:
    if smallest is None or i<smallest :
        smallest=i
"""

smallest  = None
largest = None
x=[4,5,3,1,2,90]
for i in x:
    if smallest is None or i<smallest :
        smallest=i
    else:
        largest=i
"""
for i in x:
    if largest is None or i>largest :
        largest=i
"""

print('Smallest:',smallest,'Largest:',largest)
