#print odd and even seperately
s=int(input("enter a number: "))
for i in range(1,s+1):
    if i%2==0:
        print("The even numbers are")
        print(i)
    else:
        print("The odd number are")
        print(i)
    
    