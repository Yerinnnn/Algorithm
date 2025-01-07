# 등급별 과목평점
grade_points = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

total_credit = 0
total_grade_point = 0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    
    if grade == 'P':
        continue
        
    total_credit += credit
    total_grade_point += credit * grade_points[grade]

print(total_grade_point / total_credit)