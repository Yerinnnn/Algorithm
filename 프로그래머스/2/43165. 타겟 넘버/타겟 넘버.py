def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        positive = dfs(index + 1, current_sum + numbers[index])
        negative = dfs(index + 1, current_sum - numbers[index])
        
        return positive + negative
    
    return dfs(0, 0)