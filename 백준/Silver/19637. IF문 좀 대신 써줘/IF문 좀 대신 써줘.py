import sys

def binary_search(array, target, start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if array[mid][0] >= target:
            end = mid - 1
            res = mid
        else:
            start = mid + 1
    return array[res][1]


N, M = map(int, sys.stdin.readline().split())

system = {}
for i in range(N):
    name, standard = sys.stdin.readline().split()
    system[i] = int(standard), name

for j in range(M):
    target = int(sys.stdin.readline())
    result = binary_search(system, target, 0, N-1)
    print(result)