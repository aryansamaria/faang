def amicable(n):
  sum = 0
  sum2 = 0
  for i in range(1,n//2+1):
    if n%i == 0:
      sum+=i
  for i in range(1,sum//2+1):
    if sum%i==0:
      sum2+=i
  if sum2 == n:
    return True
  else:
    False


num = int(input("Enter the number you need to check"))
if amicable(num):
  print("Yes it is amicable number")
else:
  print("No it is not")