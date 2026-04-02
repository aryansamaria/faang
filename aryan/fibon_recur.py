def fibo(n,r,a=0,b=1):
  print(a, end=',')
  if n > r:
    return
  n = a + b
  return fibo(n,r,a=b,b=n)


rannge = int(input("Ik its 50 but give me anything else range"))
n=0
fibo(n,rannge)

