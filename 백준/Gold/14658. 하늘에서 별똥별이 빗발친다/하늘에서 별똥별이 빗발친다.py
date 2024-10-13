import sys

n, m, l, k = map(int, input().split())  # n: 빌딩 수, m: 발코니 크기, l: 발코니의 위치, k: 별의 개수
arr = []  # 별의 좌표를 저장할 리스트

for _ in range(k):
    arr.append(list(map(int, input().split())))

answer = 0  # 최대 범위 내 별의 개수를 저장할 변수

for i in range(k):
    for j in range(k):
        cnt = 0  # 현재 발코니 범위에 포함된 별의 개수 초기화
        sx, sy = min(arr[i][0], arr[j][0]), min(arr[i][1], arr[j][1])  # 발코니의 좌측 상단 좌표

        for x, y in arr:
            if sx <= x <= sx + l and sy <= y <= sy + l:  # 발코니 범위 내 별 개수 세기
                cnt += 1  # 발코니 범위 내에 있는 별 개수 증가

        answer = max(answer, cnt)  # 최대 별 개수 업데이트

print(k - answer)  # 총 별 개수에서 최대 별 개수를 빼서 결과 반환