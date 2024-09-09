def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    camera_count = 0
    camera_position = float('-inf')
    
    for start, end in routes:
        # 현재 차량의 진입 지점이 이전에 설치된 카메라의 위치보다 크다면
        if start > camera_position:
            # 새 카메라를 현재 차량의 진출 지점에 설치
            camera_position = end
            camera_count += 1
    
    return camera_count