alpha = input()
result = [-1 for _ in range(26)]

for i in range(len(alpha)):
    value = ord(alpha[i]) - 97
    if result[value] == -1:
        result[value] = i

for i in result:
    print(i, end=' ')

'''alpha = input()
result = list(range(97, 123))

for i in result:
    print(alpha.find(chr(i)), end=' ')'''