def anagram(s, t):
  temp_set = set()
  temp_set2 = set()
  for i in s.lower():
    temp_set.add(i)
  for j in t.lower():
    temp_set2.add(j)
  if temp_set2 == temp_set:
    return True
  else:
    return False

test_str = input("enter the string you want to check \n")
test_str2 = input("enter the another string you want to check \n")
if anagram(test_str, test_str2):
  print("ha ha anagram he hai")
else:
  print("na bhai yo na hai")
