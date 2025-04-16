import sys

input = sys.stdin.readline

N = int(input())
numbers = sorted(int(input()) for _ in range(N))
print('\n'.join(map(str, numbers)))