def mostwater(l):
  maxx_ar = 0
  for i in range(len(l)-1):
    for j in range(i+1,len(l)):
      cal = min(l[i],l[j])*(j-i)
      if cal>maxx_ar:
        maxx_ar=cal
  return maxx_ar


li = [1,8,6,2,5,4,8,3,7]
res = mostwater(li)
print(res)