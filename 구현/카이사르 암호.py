secret = input()

for ch in secret:
    if ch == 'A' or ch == 'B' or ch == 'C':
        update_ch = chr(ord(ch) + 23)
    else:
        update_ch = chr(ord(ch) - 3)
    print(update_ch, end='')