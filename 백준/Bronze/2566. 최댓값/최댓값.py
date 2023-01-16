import sys
board =[]

for i in range(9):
    board.append(list(map(int,input().split())))

X=0
Y=0
Max =-1
for i in range(9):
    for j in range(9):
        if board[i][j]>Max:
            Max=board[i][j]
            X=i+1
            Y=j+1
print(Max)
print(X, Y)