def twosum(cdt, tar):
  for i in range(len(cdt)-1):
    sum = 0
    for j in range(i,len(cdt)):
      sum += cdt[j]
      if sum == tar:
        return f"[{i},{j}]"


l = [2,7,11,15]
t = 33
res = twosum(l,t)
print(res)