a = set(range(1, 10001))
b = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    b.add(i)
s = sorted(a - b)
for i in s:
    print(i)