def solve_n_queens(n):
    # 방문 기록 저장
    columns = [0] * n    # 각 열에 퀸을 놓을 수 있는지 여부 확인
    diagonals1 = [0] * (2 * n - 1)  # 오른쪽 위 대각선 체크
    diagonals2 = [0] * (2 * n - 1)  # 왼쪽 위 대각선 체크
    count = 0  # 가능한 배치 수를 카운트하는 변수

    def backtrack(row):
        nonlocal count
        if row == n:  # 모든 퀸을 배치했으면 경우의 수 증가
            count += 1
            return
        
        for col in range(n):  # 현재 행에서 가능한 열을 탐색
            if columns[col] or diagonals1[row + col] or diagonals2[row - col + n - 1]:
                continue  # 열 또는 대각선에 퀸이 이미 있으면 스킵
            
            # 퀸 배치
            columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = 1
            backtrack(row + 1)  # 다음 행으로 이동
            # 퀸 제거 (백트래킹)
            columns[col] = diagonals1[row + col] = diagonals2[row - col + n - 1] = 0

    backtrack(0)  # 첫 번째 행부터 시작
    return count

n = int(input())
print(solve_n_queens(n))