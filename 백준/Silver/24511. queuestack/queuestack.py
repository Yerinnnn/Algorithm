from collections import deque

N = int(input())
types = list(map(int, input().split()))
values = list(map(int, input().split()))
M = int(input())
inputs = list(map(int, input().split()))

# 큐의 역할을 하는 부분만 deque에 담음 (type이 0인 것만)
queue = deque()
for t, v in zip(types, values):
    if t == 0:
        queue.append(v)

for x in inputs:
    queue.appendleft(x)
    print(queue.pop(), end=' ')