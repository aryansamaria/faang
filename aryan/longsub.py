# Took me 1 hour 40 minutes to solve this
def longest_substring(s):
  se= set()
  left = 0
  maxx = 0
  for i in range(len(s)):
    while s[i] in se:
      se.remove(s[left])
      left+=1

    se.add(s[i])
    maxx = max(maxx, i - left + 1)
  return maxx


st = "abcabcbb"
res = longest_substring(st)
print(res)