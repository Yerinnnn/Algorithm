N = int(input().strip())

current_max = 1
layer = 1

while current_max < N:
    current_max += 6 * layer
    layer += 1

print(layer)