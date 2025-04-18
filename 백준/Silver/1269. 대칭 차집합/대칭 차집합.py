A_len, B_len = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 대칭 차집합은 ^ 또는 symmetric_difference
print(len(A ^ B))