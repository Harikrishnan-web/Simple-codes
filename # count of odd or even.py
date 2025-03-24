# count of odd or even
s=int(input("enter a number:"))
o=0
e=0
for i in range(1,s+1):
    if i%2==0:
        e=e+1
    else:
        o=o+1
print("even:",e,"odd",o)