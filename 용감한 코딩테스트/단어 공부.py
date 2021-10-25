from collections import Counter

ch = input()
result = Counter(ch.upper()).most_common()

if len(result) == 1 or result[0][1] != result[1][1]:
    print(result[0][0])
else:
    print('?')
