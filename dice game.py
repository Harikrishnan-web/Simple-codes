import random
HK = True
while HK:
    di=[0,0,0,0,0]
    for i in range(5):
        di[i] = random.randint(1,6)
        print("your dice is",di)
        di.sort()
        if di[0]==di[4]:
            print("congrats your match is fixed ")
        elif di[0]==di[3]:
            print("4 are same")
        elif di[0]==di[2]:
            print ("3 are same")
        elif di[0]==di[1]:
            print("2 are same")
        elif di[0]==di[0]:
            print("1 is same")
        ans=input("enter to contu")
        if ans=="":
            HK=True
        else:
            HK=False
        
        
        
        
        
        
        
    
