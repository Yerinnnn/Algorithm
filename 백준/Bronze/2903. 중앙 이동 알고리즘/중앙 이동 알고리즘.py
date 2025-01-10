N = int(input())

# 한 변의 점의 개수: 초기값 2에서 매 단계마다 2^N씩 증가
dots_per_side = 1 + 2**N

# 전체 점의 개수는 한 변의 점의 개수의 제곱
print(dots_per_side * dots_per_side)