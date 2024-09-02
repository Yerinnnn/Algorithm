import heapq

def solution(jobs):
    # jobs 배열을 작업 요청 시간 기준으로 정렬
    jobs.sort()
    
    # 작업 대기 큐와 현재 시간, 총 대기 시간, 처리된 작업 수 초기화
    wait_queue = []
    current_time = 0
    total_wait_time = 0
    job_index = 0
    count = 0
    
    # 모든 작업이 처리될 때까지 반복
    while count < len(jobs):
        # 현재 시간까지 요청된 작업들을 대기 큐에 추가
        while job_index < len(jobs) and jobs[job_index][0] <= current_time:
            # 대기 큐는 소요 시간 기준으로 최소 힙 구성
            heapq.heappush(wait_queue, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
            
        # 대기 큐가 비어있다면 현재 시간을 다음 작업의 요청 시간으로 이동
        if not wait_queue:
            current_time = jobs[job_index][0]
        else:
            # 대기 큐에서 가장 소요 시간이 짧은 작업을 꺼내 처리
            processing_time, request_time = heapq.heappop(wait_queue)
            current_time += processing_time  # 현재 시간 갱신
            total_wait_time += current_time - request_time  # 총 대기 시간 계산
            count += 1  # 처리된 작업 수 증가
    
    # 평균 대기 시간을 계산하여 반환
    return total_wait_time // len(jobs)