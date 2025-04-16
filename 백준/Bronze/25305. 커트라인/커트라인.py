N, K = map(int, input().split())
scores = sorted(list(map(int, input().split())), reverse=True)
print(scores[K - 1])