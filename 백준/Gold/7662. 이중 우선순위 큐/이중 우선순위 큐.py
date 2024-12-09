import sys
import heapq

input = sys.stdin.readline

def sync(heap, valid):
    # 유효하지 않은 값(다른 힙에서 이미 삭제된 값)을 제거
    while heap and not valid[heap[0][1]]:
        heapq.heappop(heap)

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    k = int(input())  # 연산의 개수
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (음수로 저장)
    valid = {}  # 값의 유효 여부를 체크하는 딕셔너리
    idx = 0  # 각 값의 고유 인덱스

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':  # 삽입 연산
            heapq.heappush(min_heap, (num, idx))  # 최소 힙에 추가
            heapq.heappush(max_heap, (-num, idx))  # 최대 힙에 음수로 추가
            valid[idx] = True  # 해당 값이 유효함을 표시
            idx += 1

        elif op == 'D':  # 삭제 연산
            if num == 1:  # 최댓값 삭제
                sync(max_heap, valid)  # 최대 힙 동기화
                if max_heap:
                    _, max_idx = heapq.heappop(max_heap)  # 최대값 삭제
                    valid[max_idx] = False  # 해당 값은 유효하지 않음으로 표시

            elif num == -1:  # 최솟값 삭제
                sync(min_heap, valid)  # 최소 힙 동기화
                if min_heap:
                    _, min_idx = heapq.heappop(min_heap)  # 최소값 삭제
                    valid[min_idx] = False  # 해당 값은 유효하지 않음으로 표시

    sync(max_heap, valid)
    sync(min_heap, valid)

    if not min_heap or not max_heap:  # 힙이 비어있으면
        print("EMPTY")
    else:  # 최댓값과 최솟값 출력
        print(-max_heap[0][0], min_heap[0][0])