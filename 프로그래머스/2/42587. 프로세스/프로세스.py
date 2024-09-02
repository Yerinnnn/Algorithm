from collections import deque

def solution(priorities, location):
    # 프로세스와 인덱스를 함께 큐에 저장
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    execution_order = 0
    
    while queue:
        # 큐의 첫 번째 프로세스 꺼내기
        current = queue.popleft()
        
        # 나머지 큐에 더 높은 우선순위가 있는지 확인
        if any(current[0] < q[0] for q in queue):
            # 더 높은 우선순위가 있다면 현재 프로세스를 큐의 끝에 추가
            queue.append(current)
        else:
            # 더 높은 우선순위가 없다면 실행
            execution_order += 1
            # 실행된 프로세스가 찾고자 하는 프로세스인 경우
            if current[1] == location:
                return execution_order