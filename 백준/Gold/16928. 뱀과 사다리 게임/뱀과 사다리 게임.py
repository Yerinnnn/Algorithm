from collections import deque

def bfs():
    # 방문 배열: 각 칸에 도달하는 최소 횟수를 기록
    visited = [0] * 101
    queue = deque([1])  # 시작점은 1번 칸
    visited[1] = 1  # 시작점 방문 표시

    while queue:
        current = queue.popleft()

        # 100번 칸에 도달하면 종료
        if current == 100:
            return visited[100] - 1

        # 주사위 던지기 (1~6)
        for dice in range(1, 7):
            next_pos = current + dice

            if next_pos <= 100:  # 게임판을 벗어나지 않도록
                # 사다리 또는 뱀을 확인
                if board[next_pos]:
                    next_pos = board[next_pos]

                # 방문하지 않은 칸만 탐색
                if not visited[next_pos]:
                    visited[next_pos] = visited[current] + 1
                    queue.append(next_pos)

N, M = map(int, input().split())
board = [0] * 101  # 게임판: 각 칸의 이동 정보를 저장

# 사다리 정보 입력
for _ in range(N):
    start, end = map(int, input().split())
    board[start] = end  # 사다리: start -> end

# 뱀 정보 입력
for _ in range(M):
    start, end = map(int, input().split())
    board[start] = end  # 뱀: start -> end

print(bfs())