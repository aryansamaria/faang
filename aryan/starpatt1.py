def ultatri(n):
  space = 0
  st = n
  for i in range(n//2+1):
    for sp in range(0,space):
      print(" ",end='')
    for sta in range(st,0,-1):
      print("*",end="")
    print()
    space+=1
    st-=2

num = int(input("enter num for ulta tri"))
ultatri(num)