# 윷놀이판의 연결 그래프와 점수 정의
graph = [
    [1], [2], [3], [4], [5],  # 빨간 경로
    [6, 21], [7], [8], [9], [10],  # 10 → 파란 경로 시작
    [11, 25], [12], [13], [14], [15],  # 20 → 파란 경로 시작
    [16, 27], [17], [18], [19], [20],  # 30 → 파란 경로 시작
    [32], [22], [23], [24], [30],  # 파란 경로들
    [26], [24], [28], [29], [24],  # 파란 경로들
    [31], [20], [32]  # 파란 경로 끝 및 도착
]

# 각 노드의 점수
score = [
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
    20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
    40, 13, 16, 19, 25, 22, 24, 28, 27, 26,
    30, 35, 0  # 0은 도착 지점
]

dice = list(map(int, input().split()))
max_score = 0  # 최대 점수를 저장


# 백트래킹 함수
def backtracking(depth, result, horses):
    global max_score
    if depth == 10:  # 주사위를 모두 굴린 경우
        max_score = max(max_score, result)
        return

    for i in range(4):  # 4개의 말 중 하나 선택
        current_pos = horses[i]  # 현재 말의 위치

        # 도착한 말은 이동 불가
        if current_pos == 32:
            continue

        # 1칸 이동
        next_pos = graph[current_pos][1] if len(graph[current_pos]) == 2 else graph[current_pos][0]

        # 남은 주사위 값을 이용해 이동
        for _ in range(1, dice[depth]):
            if next_pos == 32:  # 도착 지점에 도달한 경우
                break
            next_pos = graph[next_pos][0]

        # 이동하려는 위치가 도착이 아니면서 다른 말이 있다면 이동 불가
        if next_pos != 32 and next_pos in horses:
            continue

        # 현재 상태 저장 후 이동
        before_pos = horses[i]
        horses[i] = next_pos

        # 백트래킹 호출
        backtracking(depth + 1, result + score[next_pos], horses)

        # 상태 복구
        horses[i] = before_pos


# 백트래킹
backtracking(0, 0, [0, 0, 0, 0])  # 초기 상태: 모든 말이 시작점에 위치
print(max_score)