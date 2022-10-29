num =int(input())
numList = list(map(int,input().split()))
checkNum = int(input())
count=0
for i in numList:
  if(i==checkNum):
    count+=1
print(count)
