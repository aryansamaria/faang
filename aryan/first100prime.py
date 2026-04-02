import math

def isprime(n):
  if n <= 1:
    return False
  for i in range(2,n//2+1):
    if n%i == 0:
      return False
  else:
    return True

def first100():
  n = 2
  count = 0
  a= 0
  while count<100:
    if isprime(n):
      count+=1
      a=n
      n+=1
    else:
      n+=1
  return a

the100thprime = first100()
print(the100thprime)