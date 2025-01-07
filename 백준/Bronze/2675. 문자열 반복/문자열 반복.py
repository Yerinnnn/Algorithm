T = int(input())
for _ in range(T):
    # 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S
    R, S = input().split()
    print(''.join(char * int(R) for char in S))