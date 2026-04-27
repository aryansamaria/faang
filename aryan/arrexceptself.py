def arr_exc_self(l):
  res = []
  for i in range(len(l)):
    summ = 1
    for j in range(len(l)):
      if i == j:
        continue
      else:
        summ*=l[j]
    res.append(summ)
  return res

inp = [1,2,3,4]
ress = arr_exc_self(inp)
print(ress)