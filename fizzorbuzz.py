#fizzorbuzz a simple code that prints fizz if input is divisible by 3 and buzz if 5, fizzbuzz if both and bumber in none

x=int(input("Enter your input"))
if (x%3 == 0):
    print("Fizz")
elif (x%5==0):
    print("Buzz")
elif(x%5==0 and x%3==0):
    print("Buzzfizz")
else:
    print("Bummer")

