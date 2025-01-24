N, K = map(int, input().split())
count = 0
result = 0  # K번째 약수가 존재하지 않을 경우에는 0을 출력

for i in range(1, N+1):
    if N % i == 0:
        count += 1
        if count == K:
            result = i
            break

print(result)