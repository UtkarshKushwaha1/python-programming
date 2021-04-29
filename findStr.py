

s="""
fshkdvjhs:4343.334
sdkjvns:324.23
sdkjbskdbv:323.34
dvnnksdjfvn:893.34
csddvbdf:534.53
"""

for i in s.split():
    try:
        k=s.find(":")
        if k<0:
            raise Exception
        print(float(i[k+1:]))
    except:
        print("Error!!")