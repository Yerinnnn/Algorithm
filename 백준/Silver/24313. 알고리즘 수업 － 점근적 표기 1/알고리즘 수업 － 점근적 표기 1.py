import sys

a1, a0 = map(int, sys.stdin.readline().split())  # f(n) = a1 * n + a0
c = int(sys.stdin.readline().strip())  # g(n) = c * n
n0 = int(sys.stdin.readline().strip())  # n >= n0에서 성립해야 함

if a1 <= c and a1 + (a0 / n0) <= c:
    print(1)  # 조건을 만족하면 1 출력
else:
    print(0)  # 만족하지 않으면 0 출력