def zero(l):
  ins = 0
  for i in range(len(l)):
    if l[i] != 0:
      l[ins], l[i] = l[i], l[ins]
      ins+=1
  return l

demo_list = [0,1,0,3,12]
res = zero(demo_list)
print(res)