import sys
import math

MAX = 246912  # 2 * 123456
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

# 입력 처리 및 결과 출력
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    count = sum(1 for i in range(n + 1, 2 * n + 1) if is_prime[i])
    print(count)
