#find the domain name in a string

s="From: stephand.marquee@ucf.ac.za sat 10 Jan 2021"
k=s.find(" ")
print(s[s.find('@')+1:s.find(" ",k+1)])
