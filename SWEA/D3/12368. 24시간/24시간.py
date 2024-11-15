T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    result = (A + B) % 24
    print(f"#{test_case} {result}")