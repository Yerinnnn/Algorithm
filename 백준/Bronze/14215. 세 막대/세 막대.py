sides = list(map(int, input().split()))
sides.sort()  # 오름차순 정렬

# 가장 긴 변이 나머지 두 변의 합보다 작아야 함
if sides[2] >= sides[0] + sides[1]:
   sides[2] = sides[0] + sides[1] - 1

print(sum(sides))