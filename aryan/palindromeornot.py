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

check_num = int(input("Enter any number to check it is palindrome or not: "))
if ispalindrome(check_num):
  print("ha ha hai ye")
else:
  print("no bhai")
