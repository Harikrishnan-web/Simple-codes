l=int(input("enter ur language mark:"))
e=int(input("enter ur enlish mark:"))
cs=int(input("enter ur computer mark:"))
mat=int(input("enter ur maths mark:"))
phy=int(input("enter ur physcs mark:"))
che=int(input("enter ur chem mark:"))
s=phy/2+che/2
cut=s+mat
if cut>180:
    print(cut)
    print("you are eligible")
else:
    print("sorry")
    

