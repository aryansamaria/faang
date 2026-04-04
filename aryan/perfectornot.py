def perfect(n):
  sum=0
  for i in range(1,n//2+1):
    if n%i==0:
      sum+=i
  if sum == n:
    return True
  else:
    return False

check_num=int(input("enter the num you want to check"))
if perfect(check_num):
  print("Yes it is perfect")
else:
  print("No it is not perfect")
