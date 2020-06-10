a=input().split(" ")
b=int(a[0])
c=int(a[1])
k=1
def sai():
    print(".|.",end="")

for i in range((b-1)//2):
    for j in range((c-3)//2):
        print("-",end="")
    for l in range(k):

        sai()
    for j in range((c-3)//2):
        print("-",end="")
    print()
    c=c-6
    k=k+2
for i in range((int(a[1])-7)//2):
    print("-",end="")
print("WELCOME",end="")
for i in range((int(a[1])-7)//2):
    print("-",end="")
print()
k=k-2
c=c+6
for i in range((b-1)//2):
    for j in range((c-3)//2):
        print("-",end="")
    for l in range(k):
        sai()
    for j in range((c-3)//2):
        print("-",end="")
    print()
    c=c+6
    k=k-2
