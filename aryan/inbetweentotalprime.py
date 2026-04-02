import math

def isprime(n):
  if n <= 1:
    return False
  for i in range(2,n//2+1):
    if n%i == 0:
      return False
  else:
    return True

def inbetween(a,b):
  count = 0
  for i in range(a,b+1):
    if isprime(i):
      print(i)
      count+=1
  return count


the100thprime = inbetween(1,50)
print(the100thprime)