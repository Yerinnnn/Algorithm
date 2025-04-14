M, N = map(int, input().split())
board = [list(input()) for _ in range(M)]

def count_repaint(x, y):
    patterns = ['W', 'B']
    min_cnt = float('inf')
    
    for first in patterns:  # 'W'로 시작할지, 'B'로 시작할지
        cnt = 0
        for i in range(8):
            for j in range(8):
                # 현재 칸이 돼야 할 색
                # (행 번호 + 열 번호) % 2 == 0 이면 첫 칸과 같은
                # (행 번호 + 열 번호) % 2 == 0 이면 반대 색
                # 즉, (i + j) % 2 로 짝수/홀수를 나누면 번갈아가면서 칠하는 패턴을 만들 수 있음
                expected = first if (i + j) % 2 == 0 else ('B' if first == 'W' else 'W')
                if board[x+i][y+j] != expected:
                    cnt += 1
        min_cnt = min(min_cnt, cnt)
    return min_cnt

answer = float('inf')
for i in range(M - 7):  # 8x8이니까 M-7까지만 봐야 함
    for j in range(N - 7):
        answer = min(answer, count_repaint(i, j))

print(answer)