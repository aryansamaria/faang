def ispalindrome(n):
  dummy = n
  sum = 0
  while dummy > 0:
    rem = dummy % 10
    sum = sum*10+rem
    dummy = dummy//10
  if n == sum:
    return True
  else:
    return False

def isprime(n):
  if n <= 1:
    return False
  for i in range(2,n//2+1):
    if n%i == 0:
      return False
  else:
    return True

check_num = int(input("Enter the number you need to check"))
if ispalindrome(check_num) and isprime(check_num):
  print("yes it is pali prime")
else:
  print("No mannn")

