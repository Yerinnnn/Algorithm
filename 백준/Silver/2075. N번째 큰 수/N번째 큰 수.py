import heapq

# N×N 행렬의 크기
n = int(input().strip())

# 최소 힙을 사용하여 N번째로 큰 수를 찾기 위한 리스트
min_heap = []

# N×N 배열의 각 요소를 입력받아 처리
for _ in range(n):
    # 각 행(row)을 입력받아 리스트로 변환
    row = list(map(int, input().strip().split()))
    
    # 각 행의 숫자들을 순차적으로 처리
    for num in row:
        if len(min_heap) < n:
            # 힙의 크기가 n보다 작으면 숫자를 힙에 추가
            heapq.heappush(min_heap, num)
        else:
            # 힙의 크기가 n 이상일 때
            # 현재 숫자가 힙의 최소값보다 크면, 힙에 추가하고 최소값을 제거
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

# 최종적으로 N번째로 큰 수는 최소 힙의 루트 노드에 위치함
print(min_heap[0])