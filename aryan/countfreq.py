def cfreq(s):
  resp_store = dict()
  for i in range(len(s)):
    if s[i] in resp_store:
      continue
    count = 0
    for j in range(i,len(s)):
      if s[i]==s[j]:
        count+=1

    resp_store[s[i]] = count
  return resp_store


str = input("Enter the string")
print(cfreq(str))
