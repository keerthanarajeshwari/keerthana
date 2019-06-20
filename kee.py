n=input()
l=[]
for char in n:
  if char not in l:
    l.append(char)
print(len(l))
