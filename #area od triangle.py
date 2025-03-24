import math
a=float(input("Eneter side a:"))
b=float(input("Enter side b: "))
c=float(input("enter side c: "))
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)