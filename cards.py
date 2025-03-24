#cards
import random
su=['clubs','spades','diamonds','hearts']
fa=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
u1=input("enter your name player 1: ")
u2=input("enter your name player 2: ")
print("welcome",u1,u2)
keepgoing=True
while keepgoing:
    
    
    a=random.choice(su)
    b=random.choice(fa)
    c=random.choice(su)
    d=random.choice(fa)
    print(u1,"picked",a,d)
    print(u2,"picked",c,b)
    if fa.index(b)>fa.index(d):
        print("you won",u1)
    else:
        print("you won",u2)
    ans=input("enter to contunuew: ")
    if ans=="":
        keepgoing=True
    else:
        keepgoing=False
    
    
    
