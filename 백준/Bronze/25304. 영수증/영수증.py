ch_M=int(input())
count=int(input())

sum_M=0
for i in range(count):
    a,b=map(int,input().split())
    sum_M+= a*b

if ch_M==sum_M:
    print("Yes")
else:
    print("No")