import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '.':
        break

    stack = []
    is_balanced = True

    for char in line:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            stack.pop()

    if stack:
        is_balanced = False

    print("yes" if is_balanced else "no")