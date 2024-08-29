def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    
    return count == 0