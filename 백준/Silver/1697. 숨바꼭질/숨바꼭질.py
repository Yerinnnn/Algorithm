import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100001
visited = [False] * MAX
time = [0] * MAX  # 각 위치에 도달하는 데 걸린 시간

def bfs(start, end):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()

        if current == end:
            return time[current]

        next_positions = [current - 1, current + 1, current * 2]

        for next_pos in next_positions:
            if 0 <= next_pos < MAX and not visited[next_pos]:
                visited[next_pos] = True
                time[next_pos] += time[current] + 1
                queue.append(next_pos)

    return -1

print(bfs(N, K))