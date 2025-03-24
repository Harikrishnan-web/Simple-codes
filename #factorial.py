#factorial
n=int(input("enter a number:"))
f=1
if n<0:
    print("no fact exists:")
elif n==0:
    print("Fact is 0")
else:
    for i in range(1,n+1):
        f=f*i
    print("The fact is",f)