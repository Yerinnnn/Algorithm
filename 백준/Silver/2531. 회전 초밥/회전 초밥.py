from collections import deque

# 첫 줄에서 n, d, k, c 값을 입력받아 각각 정수로 변환
# n: 초밥의 개수, d: 초밥의 종류 수, k: 연속해서 먹을 접시 수, c: 쿠폰 번호
n, d, k, c = map(int, input().split())

# n개의 초밥 정보를 리스트로 입력받아 sushi 리스트에 저장
sushi = [int(input()) for _ in range(n)]

# 시작 인덱스(start), 끝 인덱스(end), 최대 초밥 가짓수(res)를 초기화
start, end, res = 0, 0, 0

# 현재 먹고 있는 초밥을 저장할 deque 자료구조를 초기화
arr = deque()

# 무한 루프를 돌며 조건에 따라 초밥을 먹는 과정을 구현
while True:
    # end 위치의 초밥을 deque에 추가
    # 원형 리스트처럼 사용하기 위해 모듈러 연산 사용
    arr.append(sushi[end % n])

    # 만약 먹은 초밥의 수가 k와 같아지면 (즉, k개의 초밥을 먹었을 때)
    if end - start == k-1:
        # 쿠폰 초밥을 추가로 deque에 넣음
        arr.append(c)

        # 현재 deque에 있는 초밥 가짓수를 set으로 변환하여 중복을 제거한 후, 최대 가짓수를 갱신
        res = max(res, len(set(arr)))

        # 가장 왼쪽에 있는 초밥 제거 (다음 슬라이딩 윈도우로 이동하기 위해)
        arr.popleft()

        # 추가했던 쿠폰 초밥도 제거
        arr.pop()

        # 시작 인덱스를 증가시켜 다음 슬라이딩 윈도우로 이동
        start += 1

        # 만약 시작 인덱스가 n의 배수가 되면 (즉, 한 바퀴를 모두 돌았으면) 루프 종료
        if start % n == 0:
            break

    # 끝 인덱스를 증가시켜 윈도우의 오른쪽으로 이동
    end += 1

# 최종적으로 최대 초밥 가짓수를 출력
print(res)