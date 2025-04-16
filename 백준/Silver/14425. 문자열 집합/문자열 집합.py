import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set(input().strip() for _ in range(N))

count = 0
for _ in range(M):
    word = input().strip()
    if word in S:
        count += 1

print(count)