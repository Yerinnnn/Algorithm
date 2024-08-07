import sys

N, game = sys.stdin.readline().split()
names = set()

for _ in range(int(N)):
    names.add(sys.stdin.readline().rstrip())

p = len(names)

if game == 'Y':
    print(p)    # 임스를 제외한 1명만 더 있으면 됨
elif game == 'F':
    print(p//2)     # 임스를 제외한 2명이 더 있어야 함
elif game == 'O':
    print(p//3)     # 임스를 제외한 3명이 더 있어야 함