#WAP to promt score 0.0 and 1.0 .If the score is out of range then print error msg.print a grade using the following table.
def Score(s):

        if(s>= 1.0 or s<= 0.0): 1/0
        if(s>=0.9):
            return "A"
        elif(s>=0.8):
            return "B"
        elif(s>=0.7):
            return "C"
        elif(s>=0.6):
            return "D"
        elif (s>=0.5):
            return "E"
        elif(s<0.5):
            return "F"
    
try:
    s=float(input("Enter Score Between (0.0) to (1.0):")) 
    if s>=0.0 and s<=1.0:
        print(Score(s)) 
    else:
         raise Exception
except:
    print("Bad Score")