def check(value):
    cnt = value.count('0')

    if cnt == 0:
        print('E')
    elif cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')

for _ in range(3):
    value = input()
    check(value)
