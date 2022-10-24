word = list(map(int,input().split()))

sum=0
for i in word:
  sum=sum+ (i*i)

print(sum%10)
