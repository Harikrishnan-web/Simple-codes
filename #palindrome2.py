#palindrome2
n=int(input("enter a number:"))
t=n
r=0
while t>0:
    y=input("Yes or no")
    while y==yes:
        re=t%10
        r=(r*10)+re
        t=t//10
print(r)
if n==r:
    print("palindrome")
else:
    print("Not")