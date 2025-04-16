N = int(input())
number = [list(map(int, input().split())) for _ in range(N)]
number.sort(key = lambda x: (x[0], x[1]))
for x, y in number:
    print(x, y)