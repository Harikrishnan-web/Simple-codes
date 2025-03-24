#count of vowels
string= input("enter word:")
vowels=0
consonant=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' ):
        vowels=vowels+1
    else:
        consonant=consonant+1
        
print("number of vowels:",vowels,"Number of non vowels:",consonant)