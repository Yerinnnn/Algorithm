def classify_triangle(a, b, c):
    sides = sorted([a, b, c])
    
    if sides[0] + sides[1] <= sides[2]:
        return "Invalid"
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

while True:
    sides = list(map(int, input().split()))
    
    if sides == [0, 0, 0]:
        break
    
    print(classify_triangle(*sides))