import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input().strip())
for _ in range(n):
    x = int(input().strip())
    
    if x == 0:
        # 힙에서 절댓값이 가장 작은 요소를 꺼내고, 없다면 0 출력
        if heap:
            print(heapq.heappop(heap)[1])  # 실제 값을 출력
        else:
            print(0)
    else:
        # 절댓값과 실제 값을 튜플로 묶어 힙에 삽입
        heapq.heappush(heap, (abs(x), x))