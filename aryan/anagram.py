def anagram(s, t):
  summ = 0
  sum2 = 0
  if len(s)==len(t):
    for i in range(len(s)):
      summ+=ord(s[i])
      sum2+=ord(t[i])
    if summ == sum2:
      return True
    else:
      False
  else:
    False

test_str = input("enter the string you want to check \n")
test_str2 = input("enter the another string you want to check \n")
if anagram(test_str, test_str2):
  print("ha ha anagram he hai")
else:
  print("na bhai yo na hai")
