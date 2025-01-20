# 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid if tree > mid else 0 for tree in trees)
    
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)