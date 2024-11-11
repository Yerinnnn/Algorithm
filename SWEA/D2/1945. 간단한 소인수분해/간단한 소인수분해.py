T = int(input())
primes = [2, 3, 5, 7, 11]

for test_case in range(1, T + 1):
    N = int(input())
    exponents = []

    for prime in primes:
        count = 0
        while N % prime == 0:
            N //= prime
            count += 1
        exponents.append(count)

    print(f"#{test_case} {' '.join(map(str, exponents))}")