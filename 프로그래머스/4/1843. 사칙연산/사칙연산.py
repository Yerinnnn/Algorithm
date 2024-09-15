def solution(arr):
    # 숫자와 연산자 분리
    def parse_expression(expr):
        nums = []
        ops = []
        num = ''
        for char in expr:
            if char.isdigit():
                num += char
            else:
                nums.append(int(num))
                ops.append(char)
                num = ''
        nums.append(int(num))
        return nums, ops

    # DP 초기화
    def initialize_dp(n):
        dp_min = [[float('inf')] * n for _ in range(n)]
        dp_max = [[float('-inf')] * n for _ in range(n)]
        return dp_min, dp_max
    
    def fill_dp(nums, ops, dp_min, dp_max):
        n = len(nums)
        
        # 단일 숫자에 대한 최소값과 최대값 초기화
        for i in range(n):
            dp_min[i][i] = nums[i]
            dp_max[i][i] = nums[i]
        
        # 길이 2부터 시작하여 DP 테이블 채우기
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    op = ops[k]
                    if op == '+':
                        dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                        dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    elif op == '-':
                        dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])
                        dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
        
        return dp_min[0][n - 1], dp_max[0][n - 1]

    nums, ops = parse_expression(arr)
    n = len(nums)
    dp_min, dp_max = initialize_dp(n)
    min_result, max_result = fill_dp(nums, ops, dp_min, dp_max)

    return max_result