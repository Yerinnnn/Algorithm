import sys
from collections import deque
input = sys.stdin.readline

# 수빈이의 초기 위치 a, 동생의 위치 b
a, b = map(int, input().split())

# 탐색 범위의 최대값을 100,000으로 설정 (배열 크기를 limit으로 지정)
limit = 100001

# 각 위치까지 도달하는 시간을 저장할 리스트 time 초기화
time = [0] * limit

# 너비 우선 탐색(BFS) 함수 정의
def bfs(x, y):
    q = deque()  # BFS 탐색을 위한 큐 초기화
    
    # 초기 위치 설정: 수빈이가 0일 경우 1에서 시작하도록 조정
    if x == 0:
        q.append(1)
    else:
        q.append(x)
    
    # BFS 탐색 시작
    while q:
        x = q.popleft()  # 큐에서 현재 위치를 꺼냄
        
        # 현재 위치가 동생의 위치와 같다면 해당 위치까지의 시간을 반환
        if y == x:
            return time[x]
        
        # 수빈이가 이동할 수 있는 세 가지 경우에 대해 반복문 실행
        for nx in (x-1, x+1, x*2):
            # 이동할 위치가 유효한 범위 내에 있고, 아직 방문하지 않은 경우
            if 0 <= nx < limit and time[nx] == 0:
                # 순간이동 (x*2)일 경우: 현재 시간 그대로 사용하고 큐의 왼쪽에 삽입 (우선 탐색)
                if nx == 2 * x:
                    time[nx] = time[x]
                    q.appendleft(nx)
                # 걷기 (x-1 또는 x+1)일 경우: 현재 시간 +1, 큐의 오른쪽에 삽입 (다음 탐색)
                else: 
                    time[nx] = time[x] + 1
                    q.append(nx)

# 수빈이의 위치가 0일 경우 예외 처리
if a == 0:
    if b == 0:
        print(0)  # 동생도 0에 있을 경우, 이동 필요 없음
    else:
        print(bfs(a, b) + 1)  # 수빈이의 위치가 0일 때, b까지의 시간에 +1을 해줌
else:
    print(bfs(a, b))  # 일반적인 경우 BFS 함수 호출하여 결과 출력