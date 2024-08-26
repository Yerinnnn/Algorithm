n = int(input())
ball = input()

# 최솟값을 찾기 위한 카운트를 저장할 리스트 생성
cnt = []

# 왼쪽에 연속된 'R'들을 제외한 나머지 'R'들의 수를 계산
temp = ball.lstrip('R')
cnt.append(temp.count('R'))

# 왼쪽에 연속된 'B'들을 제외한 나머지 'B'들의 수를 계산
temp = ball.lstrip('B')
cnt.append(temp.count('B'))

# 오른쪽에 연속된 'R'들을 제외한 나머지 'R'들의 수를 계산
temp = ball.rstrip('R')
cnt.append(temp.count('R'))

# 오른쪽에 연속된 'B'들을 제외한 나머지 'B'들의 수를 계산
temp = ball.rstrip('B')
cnt.append(temp.count('B'))

# 4개의 경우 중에서 최솟값을 출력
# (공의 연속된 부분을 제외한 나머지 공들의 수 중 가장 적은 값을 출력)
print(min(cnt))