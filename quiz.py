#quiz
a = """ what being is dhruv
A.Human
B.Inhuman
C.Alien
D.ruler"""
b = """ what is harikrishnan
A.Human
B.Monkey
C.Varshini's lover
D.Roshini's lover"""
c = """ What is rizwan khan
A.Human
B.dharshini's friend
C.Dhruv's BF
D.Harikrishnan BF"""
d = """ what is orador audaz
A. fearless speaker
B.fearfull speaker
C.fearless dancer
D.fearless singer"""

quest={a:"D", b:"D", c:"B", d:"A"}
name=input("Thumhra nam kya hey: ")
print("welcome my dear",name,"this is quiz")
points=10
for x in quest:
    print(x)
    f1=input("do you want to skip(YES/NO): ")
    if f1=="yes":
        continue
    ans = input("enter ur ans(A/B/C/D): ")
    if ans==quest[x]:
        print("super")
        points=points+7
        print("your score is ", points)
    else:
        print("sorry wrong ans")
        points=points-4
        print("your score is ", points)
