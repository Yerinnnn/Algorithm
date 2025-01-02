from itertools import combinations

# 축구를 하기 위해 모인 사람 N, 선수들의 능력치 S
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 모든 선수의 번호
all_players = set(range(N))

min_diff = float('inf')

# 팀 조합 생성
for team1 in combinations(all_players, N // 2):
    team2 = all_players - set(team1)  # 상대 팀

    # 능력치 계산
    def calculate_score(team):
        score = 0
        for x, y in combinations(team, 2):
            score += S[x][y] + S[y][x]
        return score

    # 각 팀의 능력치 계산
    score1 = calculate_score(team1)
    score2 = calculate_score(team2)

    # 능력치 차이 갱신
    min_diff = min(min_diff, abs(score1 - score2))

print(min_diff)