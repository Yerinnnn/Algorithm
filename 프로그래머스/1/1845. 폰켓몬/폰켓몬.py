def solution(nums):
    unique_type = len(set(nums))
    
    if len(nums) / 2 > unique_type:
        return unique_type
    else:
        return len(nums) / 2