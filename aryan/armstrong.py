def armstrong(n):
  dummy = n
  sum = 0
  l = len(str(n))
  while dummy > 0:
    rem = dummy % 10
    sum = sum + rem**l
    dummy = dummy//10
  if sum == n:
    return True
  else:
    return False


count_limit = int(input("Enter the range till"))
count = 0
num = 0
while count<count_limit:

  if armstrong(num):
    print(num)
    count+=1

  num+=1

