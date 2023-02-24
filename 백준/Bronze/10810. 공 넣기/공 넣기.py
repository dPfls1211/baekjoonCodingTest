N, M = map(int, input().split())
basket = [0] * (N+1)

for p in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k 

for i in range(1, N+1):
    print(basket[i], end = ' ')