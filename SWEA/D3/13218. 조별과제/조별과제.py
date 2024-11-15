T = int(input())

for test_case in range(1, T + 1):
    students = int(input())
    groups = students // 3
    print(f"#{test_case} {groups}")