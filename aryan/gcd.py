def gcd(a,b):
  n = min(a,b)
  for i in range(1,n//2+1):
    if a%i == 0 and b%i == 0:
      num = i
  return num


x = int(input("enter the first number\n"))
y = int(input("enter the second number\n"))
nn = gcd(x,y)
print(nn)