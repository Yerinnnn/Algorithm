def solution(n, lost, reserve):
    students = [1] * (n + 1)  # 체육복 한 개씩 가지고 있다고 가정
    
    # 도난당한 학생
    for i in lost:
        students[i] -= 1
        
    # 여벌의 체육복을 가져온 학생
    for i in reserve:
        students[i] += 1
        
    for i in range(1, n + 1):
        if students[i] == 0:  # 도난당한 학생
            if i > 1 and students[i - 1] == 2:  # 바로 앞번호의 학생
                students[i] += 1
                students[i - 1] -= 1
            elif i < n and students[i + 1] == 2:  # 바로 뒷번호의 학생
                students[i] += 1
                students[i + 1] -= 1
                
    return sum(1 for s in students[1:] if s > 0)