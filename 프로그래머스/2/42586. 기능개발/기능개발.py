import math

def solution(progresses, speeds):
    # 작업 별 완료까지 남은 일수 계산
    days_left = [
        math.ceil((100 - progress) / speed) 
        for progress, speed in zip(progresses, speeds)
    ]
    
    deployments = []
    
    current_deploy_day = days_left[0]
    count = 1
    
    for day in days_left[1:]:
        if day <= current_deploy_day:
            # 현재 배포 그룹에 포함됨
            count += 1
        else:
            # 새로운 배포 그룹 시작
            deployments.append(count)
            current_deploy_day = day
            count = 1
    
    # 마지막 배포 그룹 추가
    deployments.append(count)
    
    return deployments