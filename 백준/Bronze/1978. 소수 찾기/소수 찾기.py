N = int(input())
numbers = map(int, input().split())
count = 0

def is_prime(n):
    if n == 1:
        return False
    # 2부터 루트n까지 나누어 떨어지는지 확인
    # n의 약수가 있다면, 반드시 루트n 이하에서 발견됨
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in numbers:
    if is_prime(num):
        count += 1

print(count)