from collections import deque

def last_card(n):
    queue = deque(range(1, n + 1))
    
    while len(queue) > 1:   # 카드가 한 장 남을 때까지 반복
        queue.popleft()
        queue.append(queue.popleft())

    return queue[0]

N = int(input())
print(last_card(N))