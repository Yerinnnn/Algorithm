import sys

input = sys.stdin.readline

n = int(input().strip())

# 탑의 높이를 리스트에 저장
heights = list(map(int, input().split()))

# 결과를 저장할 리스트 (각 탑이 볼 수 있는 탑의 인덱스)
results = [0] * n

# 스택을 사용하여 인덱스를 저장
stack = []

# 각 탑을 순회하며 처리
for i in range(n):
    # 현재 탑의 높이
    current_height = heights[i]
    
    # 스택이 비어 있지 않고, 스택의 마지막 탑이 현재 탑보다 낮을 경우
    while stack and heights[stack[-1]] <= current_height:
        stack.pop()  # 스택에서 낮은 탑 제거
    
    # 스택이 비어 있지 않으면, 스택의 탑이 현재 탑보다 높은 탑임
    if stack:
        results[i] = stack[-1] + 1  # 인덱스는 1부터 시작하므로 +1
    
    # 현재 탑의 인덱스를 스택에 추가
    stack.append(i)

print(' '.join(map(str, results)))