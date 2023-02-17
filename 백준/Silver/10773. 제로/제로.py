sums=0
n=int(input())
N_list=[]
for i in range(n):
    j= int(input())
    if(j==0):
        N_list.pop()
    else:
        N_list.append(j)

print(sum(N_list))
