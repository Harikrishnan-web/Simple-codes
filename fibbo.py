n=int(input("enter number of terms:"))
n1,n2=0,1
c=0
if n<=0:
    print("please enter a positive number")
elif n==1:
    print("the fibbonacy series of",n,"is",n1)
else:
    print("the fibbonacy series is:")
    while c<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1