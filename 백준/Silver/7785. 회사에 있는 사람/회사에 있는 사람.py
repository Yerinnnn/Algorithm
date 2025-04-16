import sys
input = sys.stdin.readline

N = int(input())
office = set()

for _ in range(N):
    name, status = input().strip().split()
    if status == 'enter':
        office.add(name)
    else:
        office.remove(name)

for name in sorted(office, reverse=True):
    print(name)