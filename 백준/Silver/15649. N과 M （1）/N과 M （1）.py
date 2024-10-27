n, m = map(int, input().split())
visited = [False] * (n + 1)  # 방문 여부 체크
result = []  # 현재 선택된 숫자들을 담을 리스트

def backtrack():
    # 순열 길이가 m에 도달하면 결과 출력
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    # 1부터 n까지 숫자 선택
    for i in range(1, n + 1):
        if not visited[i]:  # 방문하지 않은 숫자만 선택
            visited[i] = True
            result.append(i)
            backtrack()  # 재귀 호출로 다음 숫자 선택
            # 백트래킹 수행: 직전 상태로 복귀
            result.pop()
            visited[i] = False

backtrack()