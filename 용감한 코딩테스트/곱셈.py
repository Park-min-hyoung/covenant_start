a = int(input())
b = int(input())
b_array = [int(i) for i in str(b)]

b_array.reverse()
for i in range(len(b_array)):
    print(a * b_array[i])

print(a * b)
