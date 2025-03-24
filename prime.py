h=int(input("Enter a number:"))
f=False
if h>1:
    for i in range(2,h):
        if(h%i)==0:
            f=True
            break
if f:
    print("Not prime")
else:
    print("prime")
