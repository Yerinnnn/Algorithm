# 바구니의 개수 N, 공을 넣는 횟수 M
N, M = map(int, input().split())
baskets = [0] * N

for _ in range(M):
    # i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다
    i, j, k = map(int, input().split())
    baskets[i-1:j] = [k] * (j-i+1)

print(*baskets)