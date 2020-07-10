n=int(input())
co=0
for i in range(1,n+1):
    inp=int(input())
    for i in range(1,inp+1):
        co+=i
        if co>=inp and co<=inp+3:
             print(i)
