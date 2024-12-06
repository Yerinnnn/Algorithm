import sys
input = sys.stdin.read

def coordinate_compression(arr):
    # 고유한 값만 추출하여 정렬
    unique_sorted = sorted(set(arr))
    # 값 -> 압축된 좌표로 매핑
    coordinate_map = {value: idx for idx, value in enumerate(unique_sorted)}
    # 원래 배열의 값을 압축된 값으로 변환
    return [coordinate_map[value] for value in arr]

n, *arr = map(int, input().split())
result = coordinate_compression(arr)

print(" ".join(map(str, result)))