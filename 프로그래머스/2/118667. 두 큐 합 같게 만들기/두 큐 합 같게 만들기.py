from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)  # 큐를 deque로 변환
    sum1, sum2 = sum(q1), sum(q2)  # 두 큐의 합 계산
    target = (sum1 + sum2) // 2  # 목표 합 (합이 홀수면 -1 반환)
    
    if (sum1 + sum2) % 2 == 1:  
        return -1  

    cnt, max_moves = 0, len(q1) * 3  # 최대 이동 횟수 제한

    # 투 포인터 기법을 위한 인덱스
    while sum1 != sum2 and cnt < max_moves:
        if sum1 > sum2:  
            num = q1.popleft()  # q1에서 pop
            sum1 -= num
            sum2 += num
            q2.append(num)  # q2에 추가
        else:
            num = q2.popleft()  # q2에서 pop
            sum2 -= num
            sum1 += num
            q1.append(num)  # q1에 추가
        cnt += 1  # 연산 횟수 증가

    return cnt if sum1 == sum2 else -1  # 목표에 도달하면 cnt, 아니면 -1 반환