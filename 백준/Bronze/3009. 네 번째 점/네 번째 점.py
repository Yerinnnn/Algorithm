x_coords = []
y_coords = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)
    
for x in x_coords:
    if x_coords.count(x) == 1:
        result_x = x

for y in y_coords:
    if y_coords.count(y) == 1:
        result_y = y
        
print(result_x, result_y)