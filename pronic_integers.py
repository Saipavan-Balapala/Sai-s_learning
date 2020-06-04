n=input()
l=[]
s=""
for i in range(4500):
    for j in range(i+1):
        if j*(j+1)==i:
            l.append(i)
while len(n)>0:
    if n[0]=="0":
        print("0",end=" ")
    else:
        for i in n:
            s+=i
            if int(s) in l:
                print(s,end=" ")

    n=n[1::1]
    s=""
