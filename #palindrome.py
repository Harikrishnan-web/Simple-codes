n = int(input("Enter a number: "))
t=n
r = 0
while t> 0:
    re = t % 10
    r = (r * 10) + re
    t = t // 10
print(r)
if n == r:
  print('Palindrome')
else:
  print("Not Palindrome")
