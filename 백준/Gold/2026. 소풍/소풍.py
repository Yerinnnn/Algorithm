def is_friend(selected, student):
    # 이미 선택된 학생들과 모두 친구인지 확인
    for s in selected:
        if not friends[s][student]:
            return False
    return True

def backtrack(selected, start):
    if len(selected) == K:  # K명을 모두 선택했으면
        for s in selected:
            print(s)
        return True
    
    for i in range(start, N+1):
        if not used[i] and friend_count[i] >= K-1 and is_friend(selected, i):
            used[i] = True
            selected.append(i)
            if backtrack(selected, i+1):  # 다음 학생 선택
                return True
            used[i] = False
            selected.pop()
            
    return False

K, N, F = map(int, input().split())
friends = [[False]*(N+1) for _ in range(N+1)]  # 친구 관계
friend_count = [0]*(N+1)  # 각 학생의 친구 수

# 친구 관계 입력
for _ in range(F):
    a, b = map(int, input().split())
    friends[a][b] = friends[b][a] = True
    friend_count[a] += 1
    friend_count[b] += 1

used = [False]*(N+1)  # 학생 선택 여부

if not backtrack([], 1):  # 1번 학생부터 시작
    print(-1)