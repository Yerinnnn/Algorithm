import sys
from collections import deque

def can_reach(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    # 두 위치 사이의 거리가 1000m 이하면 True
    return abs(x1 - x2) + abs(y1 - y2) <= 1000

def bfs(home, stores, festival):
    queue = deque([home])  # 시작점 (집)
    visited = set()
    
    while queue:
        x, y = queue.popleft()
        
        # 만약 페스티벌에 도착 가능하면 happy 출력 후 종료
        if can_reach((x, y), festival):
            print("happy")
            return
        
        # 편의점 탐색
        for i in range(len(stores)):
            if i not in visited and can_reach((x, y), stores[i]):
                visited.add(i)
                queue.append(stores[i])
                
    # BFS가 끝났는데도 페스티벌에 도착 못 하면 sad 출력
    print("sad")
        
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    home = tuple(map(int, sys.stdin.readline().split()))
    stores = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    festival = tuple(map(int, sys.stdin.readline().split()))
    
    bfs(home, stores, festival)