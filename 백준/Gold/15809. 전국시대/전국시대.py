import sys
 
N, M = map(int, sys.stdin.readline().split())
conturies = [0]
for _ in range(N):
    conturies.append(int(sys.stdin.readline()))
 
 
def find(n):
    now = conturies[n]
    if now < 0:
        return find(-1*now)
    else:
        return n
 
for _ in range(M):
    com, x, y = map(int, sys.stdin.readline().split())
    find_x = find(x)
    find_y = find(y)
 
    if com == 1:
        conturies[find_x] += conturies[find_y]
        conturies[find_y] = -1*find_x
 
    else:
        if conturies[find_x] == conturies[find_y]:
            conturies[find_x] = 0
            conturies[find_y] = 0
        elif conturies[find_x] > conturies[find_y]:
            conturies[find_x] -= conturies[find_y]
            conturies[find_y] = -1*find_x
        else:
            conturies[find_y] -= conturies[find_x]
            conturies[find_x] = -1*find_y
 
answer = []
for i in conturies:
    if i > 0:
        answer.append(i)
answer.sort()
print(len(answer))
print(*answer)