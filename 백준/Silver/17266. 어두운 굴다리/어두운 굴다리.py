import sys
import math

N = int(input())    # 굴다리의 길이
M = int(input())    # 가로등의 개수
x = list(map(int, input().split()))    # M 개의 설치할 수 있는 가로등의 위치(오름차순, 중복 X, 정수)

res = x[0]
for i in range(1, M):
    res = max(res, math.ceil((x[i] - x[i - 1]) / 2))
res = max(res, N - x[-1])

print(res)     # 굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력