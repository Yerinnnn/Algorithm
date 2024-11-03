# 소수 판별
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 팰린드롬 판별
def is_palindrome(n):
    return str(n) == str(n)[::-1]

N = int(input())

while True:
    if is_prime(N) and is_palindrome(N):
        print(N)
        break
    N += 1