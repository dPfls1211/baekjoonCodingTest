num=int(input())

for i in range(num):
    N,S=input().split()
    
    for j in S:
        print(j*int(N), end='')
    print()