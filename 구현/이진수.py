case = int(input())
for _ in range(case):
    n = int(input())
    binary = list(bin(n)[2:])
    binary.reverse()

    for i in range(len(binary)):
        if binary[i] == '1':
            print(i, end=' ')
    print()

'''for i in range(len(binary)):
    if binary[-i - 1] == '1':
        print(i, end=' ')'''