from itertools import permutations
s=input()
l=[]
a=""
for i in s:
    if i.isnumeric():
        l.append(i)
l=list(set(l))
l1=list(permutations(l,len(l)))
l=[]
for i in l1:
    i=list(i)
    a=int(''.join(i))
    if a%2==0:
        l.append(a)
if len(l)>=1:
    print(max(l))
else:
    print(-1)
