import sys
import heapq

N = int(sys.stdin.readline())  # 기존 작업의 개수
work = []  # 기존 작업을 저장하는 우선순위 큐 (마감 시간, 작업 시간)
for _ in range(N):
    t, d = map(int, sys.stdin.readline().split())  # 작업 시간 t, 마감 시간 d
    heapq.heappush(work, (d, t))  # 마감 시간을 기준으로 최소 힙에 삽입

M = int(sys.stdin.readline())  # 추가 작업의 개수 입력
plus_work = []  # 추가 작업을 저장할 우선순위 큐 (시작 시간, 마감 시간, 작업 시간)
for _ in range(M):
    w, t, d = map(int, sys.stdin.readline().split())  # 시작 시간 w, 작업 시간 t, 마감 시간 d
    heapq.heappush(plus_work, (w, d, t))  # 시작 시간을 기준으로 최소 힙에 삽입

current_time = 0  # 현재 시간 초기화

# 작업 처리 루프
while work or plus_work:  # 기존 작업과 추가 작업이 모두 처리될 때까지 반복
    # 현재 시간이 도달한 추가 작업을 기존 작업 큐에 이동
    while plus_work and plus_work[0][0] <= current_time:  # 시작 시간이 현재 시간 이하인 작업
        w, d, t = heapq.heappop(plus_work)  # 추가 작업 추출
        heapq.heappush(work, (d, t))  # 기존 작업 큐에 삽입 (마감 시간 기준)

    # 기존 작업이 없으면 현재 시간을 다음 추가 작업의 시작 시간으로 이동
    if not work:
        if plus_work:  # 아직 처리하지 않은 추가 작업이 남아있을 경우
            current_time = plus_work[0][0]  # 현재 시간을 다음 추가 작업의 시작 시간으로 업데이트
        continue  # 다음 루프로 이동

    # 현재 작업 처리
    d, t = heapq.heappop(work)  # 가장 마감 시간이 빠른 작업 추출

    # 추가 작업 중 우선 처리해야 할 작업을 확인
    while plus_work and plus_work[0][0] < current_time + t:  # 추가 작업의 시작 시간이 현재 작업 중간에 도달
        w, D, T = heapq.heappop(plus_work)  # 추가 작업 추출

        # 추가 작업의 마감 시간이 더 급하면 현재 작업을 나눠서 처리
        if w < current_time + t and D < d:  # 추가 작업이 더 긴급한 경우
            remaining_t = t - (w - current_time)  # 현재 작업의 남은 처리 시간 계산
            if remaining_t > 0:
                heapq.heappush(work, (d, remaining_t))  # 나머지 작업을 다시 큐에 삽입

            # 추가 작업 수행
            t = T  # 현재 작업을 추가 작업으로 교체
            d = D  # 현재 마감 시간을 추가 작업의 마감 시간으로 교체
            current_time = w  # 현재 시간을 추가 작업의 시작 시간으로 업데이트

        else:
            heapq.heappush(plus_work, (w, D, T))  # 추가 작업을 다시 큐에 삽입
            break  # 더 이상 처리할 추가 작업이 없으므로 루프 종료

    # 현재 작업이 마감 시간 내에 완료되지 못하면 실패
    if current_time + t > d:
        print("NO")  # 작업을 마감 시간 내에 완료할 수 없음
        sys.exit()  # 프로그램 종료

    current_time += t  # 작업 완료 후 현재 시간을 업데이트

# 모든 작업을 마감 시간 내에 완료한 경우
print("YES")
print(current_time)