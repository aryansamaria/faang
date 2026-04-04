def seperate(n):
  sum = 0
  for i in str(n):
    sum+=int(i)
  return sum

def verify(n):
  l = seperate(n)
  if len(str(l)) == 1:
    return l
  else:
    return verify(l)


check_num = int(input("enter the number you need to check"))
res = verify(check_num)
print(res)