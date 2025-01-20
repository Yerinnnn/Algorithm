N, M = map(int, input().split())

no_hear = set(input() for _ in range(N))
no_see = set(input() for _ in range(M))

result = sorted(no_hear & no_see)

print(len(result))
for name in result:
    print(name)