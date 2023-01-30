import sys

N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e
    
#시작시간 정렬뒤, 다시 끝나는 시간으로 정렬
#정렬이 끝난시간 우선순위임 끝나는걸 먼저봐야 더 많은 회의 가능
time.sort(key = lambda x: (x[1], x[0])) 

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)

#n = int(input())
#time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
#ans = end = 0
#for s, e in time:
#    if s >= end:
#        ans += 1
#        end = e
#print(ans)