case = int(input())
for _ in range(case):
    ch = input().split()

    for i in range(len(ch)):
        print(ch[i][::-1], end=' ')
    print()

case = int(input())

'''for _ in range(case):
    ch = input()
    ch += " "
    stack = []

    for j in ch:
        if j != " ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')'''