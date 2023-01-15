num=int(input())
numList=list(map(int,input().split()))

Glist=[]
before=0
Gcount=0
Mlists=[]
for i in numList:
    if before!=i-1:
        Mlists.append(Glist)
        Glist=[]
    Glist.append(i)
    
    before=i
Mlists.append(Glist)
Mlists.pop(0)
sus=0
for j in Mlists:
    sus+=j[0]
print(sus)
