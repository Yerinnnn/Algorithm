import heapq

def solution(operations):
    # 최소 힙과 최대 힙을 각각 선언
    min_heap = []
    max_heap = []
    
    # 각 명령어에 해당하는 값이 유효한지 여부를 체크할 리스트
    visited = [False] * len(operations)

    # 주어진 모든 명령어를 처리
    for i, operation in enumerate(operations):
        if operation[0] == 'I':  # 명령어가 'I'로 시작하면 숫자 삽입
            num = int(operation[2:])  # 숫자를 추출
            # 최소 힙과 최대 힙에 각각 삽입
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            # 삽입된 숫자를 유효한 상태로 설정
            visited[i] = True
        elif operation == 'D 1':  # 명령어가 'D 1'인 경우 최대값 삭제
            # 최대 힙에서 유효하지 않은 값들을 제거
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:  # 최대값이 유효하다면
                visited[max_heap[0][1]] = False  # 해당 값을 비활성화
                heapq.heappop(max_heap)  # 최대값 제거
        elif operation == 'D -1':  # 명령어가 'D -1'인 경우 최솟값 삭제
            # 최소 힙에서 유효하지 않은 값들을 제거
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:  # 최솟값이 유효하다면
                visited[min_heap[0][1]] = False  # 해당 값을 비활성화
                heapq.heappop(min_heap)  # 최솟값 제거

    # 모든 명령어를 처리한 후, 유효한 최소값과 최대값을 찾음
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 결과 반환
    if min_heap and max_heap:  # 유효한 최솟값과 최댓값이 존재할 경우
        return [-max_heap[0][0], min_heap[0][0]]  # 최대값, 최소값 반환
    else:
        return [0, 0]  # 힙이 비어있는 경우 [0, 0] 반환