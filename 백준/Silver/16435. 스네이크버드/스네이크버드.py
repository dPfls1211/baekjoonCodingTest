n, l = map(int,input().split())

fruits = list(map(int,input().split()))
fruits.sort()
for i in range(n):
    if fruits[i] <= l:
        l += 1
    else:
        break
print(l)