N = int(input())
numbers = list(map(int, input().split()))
# +, -, *, / 연산자 개수
operators = list(map(int, input().split()))

max_result = float('-inf')
min_result = float('inf')

def dfs(depth, result):
    global max_result, min_result
    
    if depth == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
        
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:  # 덧셈
                dfs(depth + 1, result + numbers[depth])
            elif i == 1:  # 뺄셈
                dfs(depth + 1, result - numbers[depth])
            elif i == 2:  # 곱셈
                dfs(depth + 1, result * numbers[depth])
            else:  # 나눗셈
                # 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꿈
                if result < 0:
                    dfs(depth + 1, -(-result // numbers[depth]))
                else:
                    dfs(depth + 1, result // numbers[depth])
            operators[i] += 1

dfs(1, numbers[0])
print(max_result)
print(min_result)