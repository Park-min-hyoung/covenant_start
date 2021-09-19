case = int(input())

for _ in range(case):
    vps = input()
    stack = []

    for i in vps:
        if i == '(':
            stack.append('(')
        else:
            if '(' in stack:
                stack.pop()
            else:
                stack.append(')')

    if stack:
        print('NO')
    else:
        print('YES')