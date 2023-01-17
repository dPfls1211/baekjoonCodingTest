T=int(input())
testCus=[]
for i in range(T):
    testCus.append(list(map(int,input().split())))


for j in testCus:
    num=0
    if j[2]%j[0] ==0:
        num+=j[2]//j[0]
        num+=100*j[0]
    else:
        num+=j[2]//j[0]+1
        num+=100*(j[2]%j[0])
    print(num)