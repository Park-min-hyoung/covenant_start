from sys import stdin
n = int(stdin.readline().strip())

stack = []
for _ in range(n):
    command = stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])

# 틀렸음(v)
'''
1. 1개 입력과 2개 입력을 동시에 하려면 처음부터 변수 2개를 통해 입력 받기보다는
동적으로 입력 받을 수 있는 '리스트'를 이용해서 변수를 입력 받는다
2. 코드가 맞는것 같은데 시간 초과가 나는 경우에는 from sys import stdin을 이용해
입력 부분을 수정해서 제출해본다'''