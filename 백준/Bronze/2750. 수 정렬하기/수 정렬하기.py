num=int(input())
lists=[]
for i in range(num):
    n=int(input())
    lists.append(n)
lists=sorted(lists)
for j in lists:
    print(j)

""" 버블
num=int(input())
lists=[]
for i in range(num):
    n=int(input())
    lists.append(n)
for i in range(len(lists)):
    for j in range(len(lists)):
        if lists[i]< lists[j]:
            lists[i], lists[j]=lists[j], lists[i]
for j in lists:
    print(j)
"""

""" 삽입
num=int(input())
lists=[]
for i in range(num):
    n=int(input())
    lists.append(n)
for i in range(1,len(lists)):
    while(i>0)&(lists[i]<lists[i-1]):
        lists[i], lists[i-1]=lists[i-1], lists[i]
        i-=1
        

for j in lists:
    print(j)
"""