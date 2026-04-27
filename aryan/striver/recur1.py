#Backtracking
def print_name(i,n):
  if i>n:
    return
  print_name(i+1,n)
  print(i, end="\n")

i = 1
n = int(input("enter"))
print_name(i,n)
