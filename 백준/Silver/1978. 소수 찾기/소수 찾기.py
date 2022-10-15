num = int(input())
pr_list = list(map(int, input().split()))

count=0
for pr in pr_list:
    if pr != 1:
        for n in range(2,pr):
            if pr % n == 0:
                break
        else:
            count+=1
        
print(count)
