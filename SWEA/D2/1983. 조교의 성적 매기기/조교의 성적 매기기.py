T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    # 학생수 N, 학점을 알고싶은 학생의 번호 K
    N, K = map(int, input().split())
    scores = []
    
    for student_num in range(1, N+1):
        midterm, final, homework = map(int, input().split())
        score = midterm * 0.35 + final * 0.45 + homework * 0.2
        scores.append((score, student_num))
        
    scores.sort(reverse = True, key = lambda x: x[0])
    
    students_per_grade = N // 10
    
    for rank, (score, student_num) in enumerate(scores):
        if student_num == K:
            grade_index = rank // students_per_grade
            print(f"#{test_case} {grades[grade_index]}")
            break