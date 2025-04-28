def cantor(start, end):
    if end - start < 3:
        return
    third = (end - start) // 3
    for i in range(start + third, start + 2 * third):
        line[i] = ' '
    cantor(start, start + third)
    cantor(start + 2 * third, end)

while True:
    try:
        n = int(input())
        size = 3 ** n
        line = ['-'] * size
        cantor(0, size)
        print(''.join(line))
    except EOFError:
        break