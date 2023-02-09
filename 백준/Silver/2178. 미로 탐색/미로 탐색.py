from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return graph[N-1][M-1]

print(bfs(0, 0))


##BFS
#from sys import stdin
#N, M = map(int, stdin.readline().split())
# matrix 배열
#matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
#visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
#dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
#queue = [(0,0)]
#visited[0][0] = 1

#while queue:
#    x, y = queue.pop(0)

#    if x == N-1 and y == M-1:
        # 최종 경로 도착
#        print(visited[x][y])
#        break

#    for i in range(4):
#        nx = x + dx[i]
#        ny = y + dy[i]
#        if 0 <= nx < N and 0 <= ny < M:
#            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
#                visited[nx][ny] = visited[x][y] + 1
#                queue.append((nx,ny))