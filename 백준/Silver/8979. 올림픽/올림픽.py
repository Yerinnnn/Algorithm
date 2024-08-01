def calculate_rank(countries, k):
    sorted_countries = sorted(countries, key=lambda x: (-x[1], -x[2], -x[3]))

    ranks = {}
    current_rank = 1
    for i, country in enumerate(sorted_countries):
        # 첫 번째 국가(i=0)는 이전 국가가 없으므로, i > 0으로 첫 번째 국가를 건너뜀
        # 현재 국가와 이전 국가의 메달 정보가 같지 않다면, 다른 등수 부여
        if i > 0 and country[1:] != sorted_countries[i-1][1:]:
            current_rank = i + 1
        ranks[country[0]] = current_rank    # ex) ranks[1번 국가] = 3등
    
    return ranks[k]

N, K = map(int, input().split())
countries = []

for _ in range(N):
    country = list(map(int, input().split()))
    countries.append(country)
    
print(calculate_rank(countries, K))