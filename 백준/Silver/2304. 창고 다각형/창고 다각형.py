# 기둥의 개수 n을 표준 입력으로 입력 받음
n = int(input().strip())

# 기둥들의 위치와 높이를 입력받아 리스트에 저장
# 각 기둥은 (위치, 높이) 형태의 튜플로 저장됨
pillars = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 기둥들을 x축 기준으로 오름차순으로 정렬
pillars.sort()

# 가장 높은 기둥을 찾음
# max_height는 현재까지 발견된 최대 높이
# max_index는 최대 높이를 가진 기둥의 인덱스
max_height = 0
max_index = 0
for i in range(n):
    if pillars[i][1] > max_height:  # 현재 기둥의 높이가 max_height보다 크면
        max_height = pillars[i][1]  # max_height를 갱신함
        max_index = i  # max_index를 현재 기둥의 인덱스로 갱신함

# 면적 계산 변수 초기화
result = 0

# 왼쪽 부분 면적 계산
# 첫 번째 기둥부터 가장 높은 기둥까지의 면적을 계산
# height는 현재까지의 최대 높이를 저장
height = pillars[0][1]
for i in range(1, max_index + 1):
    if pillars[i][1] > height:  # 다음 기둥의 높이가 현재 높이보다 클 경우,
        result += height * (pillars[i][0] - pillars[i - 1][0])  # 현재 높이로 면적을 계산하고 더함
        height = pillars[i][1]  # 높이 갱신
    else:
        result += height * (pillars[i][0] - pillars[i - 1][0])  # 그렇지 않을 경우, 현재 높이로 면적을 계산함

# 오른쪽 부분 면적 계산
# 마지막 기둥부터 가장 높은 기둥까지의 면적을 계산
height = pillars[-1][1]
for i in range(n - 2, max_index - 1, -1):
    if pillars[i][1] > height:  # 이전 기둥의 높이가 현재 높이보다 클 경우,
        result += height * (pillars[i + 1][0] - pillars[i][0])  # 현재 높이로 면적을 계산하고 더함
        height = pillars[i][1]  # 높이를 갱신함
    else:
        result += height * (pillars[i + 1][0] - pillars[i][0])  # 그렇지 않을 경우, 현재 높이로 면적을 계산

# 가장 높은 기둥의 면적을 추가
# 가장 높은 기둥 부분은 중복되거나 누락되지 않게 처리됨
result += max_height

# 최종적으로 계산된 면적을 출력
print(result)