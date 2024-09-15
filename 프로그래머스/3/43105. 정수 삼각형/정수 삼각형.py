def solution(triangle):
    # 삼각형의 크기
    n = len(triangle)
    
    # 삼각형을 변경하여 동적 프로그래밍을 통해 최대 합을 계산
    # 삼각형의 마지막 행부터 시작하여, 위쪽으로 계산해나감
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 현재 위치에서 가능한 최대 합을 계산
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    # 삼각형의 최상단 위치의 값이 최대 합
    return triangle[0][0]
