import sys
from collections import deque

def bfs(S):
    queue = deque([(1, 0, 0)])  # (이모티콘 개수, 클립보드 개수, 연산 횟수)
    visited = set()
    visited.add((1, 0))  # 초기 상태 방문 처리
    
    while queue:
        screen, clipboard, time = queue.popleft()

        # 목표 도달 시 종료
        if screen == S:
            return time
        
        # 복사: 현재 화면의 이모티콘을 클립보드에 저장
        if (screen, screen) not in visited:
            visited.add((screen, screen))
            queue.append((screen, screen, time + 1))

        # 붙여넣기: 클립보드의 내용을 현재 화면에 추가 (단, 0개는 제외)
        if clipboard > 0 and (screen + clipboard, clipboard) not in visited:
            visited.add((screen + clipboard, clipboard))
            queue.append((screen + clipboard, clipboard, time + 1))

        # 삭제: 이모티콘 1개 삭제
        if screen > 1 and (screen - 1, clipboard) not in visited:
            visited.add((screen - 1, clipboard))
            queue.append((screen - 1, clipboard, time + 1))

S = int(sys.stdin.readline().strip())
print(bfs(S))