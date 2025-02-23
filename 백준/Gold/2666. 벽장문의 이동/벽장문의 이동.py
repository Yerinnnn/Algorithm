import sys

n = int(sys.stdin.readline().strip())  # 벽장의 개수
open1, open2 = map(int, sys.stdin.readline().split())  # 현재 열려 있는 두 개의 벽장
m = int(sys.stdin.readline().strip())  # 열어야 할 벽장의 개수
orders = [int(sys.stdin.readline().strip()) for _ in range(m)]

def solve(n, open1, open2, orders):
    # dp[left][right][idx] : left와 right 두 개의 열린 문이 있을 때, idx 번째 문을 여는 최소 이동 횟수를 저장
    # 아직 방문하지 않은 상태 표시를 위해 -1로 초기화
    dp = [[[-1] * (len(orders) + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    
    def dfs(left, right, idx):
        # 모든 문을 연 경우, 더 이상 이동할 필요 없음
        if idx == len(orders):
            return 0
        
        # 이미 계산된 경우 값 반환 (메모이제이션)
        if dp[left][right][idx] != -1:
            return dp[left][right][idx]
        
        target = orders[idx]  # 현재 열어야 할 문
        
        # 왼쪽 문을 움직여서 target을 여는 경우
        move_left = abs(left - target) + dfs(target, right, idx + 1)
        
        # 오른쪽 문을 움직여서 target을 여는 경우
        move_right = abs(right - target) + dfs(left, target, idx + 1)
        
        # 둘 중 최소 이동 횟수를 선택하여 저장
        dp[left][right][idx] = min(move_left, move_right)
        return dp[left][right][idx]
    
    return dfs(open1, open2, 0)

print(solve(n, open1, open2, orders))