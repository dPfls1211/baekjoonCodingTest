import sys


n = int(sys.stdin.readline())
temp = dict() # 딕셔너리

#출입 기록을 확인
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    # 출입을 했으면 딕셔너리에 추가
    if b == "enter":
        temp[a] = b
    # 퇴근을 했으면 삭제
    else:
        del temp[a]

# 사전 순의 역순으로 정렬
temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)