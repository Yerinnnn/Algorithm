import math
import sys
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # M개의 사이트 중 N개를 선택하는 조합 계산
    result = math.comb(m, n)
    print(result)