#Anagram1
def check(s1,s2):
    if (sorted(s1)==sorted(s2)):
       print("Angram")
    else:
       print("Not")

s1=input("Word:")
s2=input("word:")
check(s1,s2)