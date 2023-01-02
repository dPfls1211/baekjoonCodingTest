#a+bx<cx
#a<(c-b)x
#a/(c-b) <x
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))