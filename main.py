s, a, b = input(), input(), input()
# s, a, b = 'ababac', 'c', 'c'
count = 0

while count <= 1000:
    if a in s:
        s = s.replace(a, b)
        count += 1
    else:
        break

if count <= 1000:
    print(count)
else:
    print('Impossible')
