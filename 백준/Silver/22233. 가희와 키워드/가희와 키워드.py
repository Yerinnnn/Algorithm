import sys

def process_keywords(N, M):
    # 키워드를 저장할 사전
    memo = {}
    answer = 0

    # 키워드 초기화
    for _ in range(N):
        keyword = sys.stdin.readline().rstrip()
        memo[keyword] = 1  # 아직 사용되지 않은 키워드로 표시
        answer += 1

    # 블로그 글 처리
    for _ in range(M):
        post = sys.stdin.readline().rstrip().split(',')
        for word in post:
            if word in memo:
                if memo[word] == 1:
                    memo[word] = 0  # 사용된 키워드로 표시
                    answer -= 1
        print(answer)  # 남아있는 키워드의 수 출력

# 입력 처리
N, M = map(int, sys.stdin.readline().split())
process_keywords(N, M)