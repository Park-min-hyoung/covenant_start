n = int(input())

for i in range(n):
    print(' ' * i + '*' * ((n * 2) - (i * 2 + 1)))