import sys
input = sys.stdin.readline

n = int(input())  # 교실 크기
arr = []  # 교실 정보를 저장할 리스트
professor = None  # 교수님 위치
seong_gyu = None  # 성규 위치

# 교실 정보를 입력받고 교수님과 성규 위치 저장
for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)
    if 5 in nums:  # 교수님 위치 (값 5)
        professor = (nums.index(5), i)  # (열, 행) 형태로 저장
    if 2 in nums:  # 성규 위치 (값 2)
        seong_gyu = (nums.index(2), i)  # (열, 행) 형태로 저장

# 교수님과 성규 위치의 최소/최대 범위 계산
x1, x2 = min(professor[0], seong_gyu[0]), max(professor[0], seong_gyu[0])
y1, y2 = min(professor[1], seong_gyu[1]), max(professor[1], seong_gyu[1])

# 교수님과 성규 사이의 학생 수 세기
student_count = 0
for y in range(y1, y2 + 1):
    student_count += arr[y][x1:x2 + 1].count(1)  # 학생(값 1) 수 세기

# 조건 확인
distance_squared = (professor[0] - seong_gyu[0]) ** 2 + (professor[1] - seong_gyu[1]) ** 2
if student_count >= 3 and distance_squared >= 25:
    print(1)  # 위험
else:
    print(0)  # 안전