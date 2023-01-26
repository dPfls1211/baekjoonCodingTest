from collections import Counter
import sys

num=int(sys.stdin.readline())

C=[]
for i in range(num):
    C.append(int(sys.stdin.readline()))
avg=round(sum(C)/len(C))
print(avg)
C.sort()
print(C[len(C)//2])
cnt = Counter(C).most_common(2)
if len(C)>1:
    if cnt[0][1] ==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(C) - min(C))
