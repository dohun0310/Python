r = int(input())
l = []
for i in range(r):
    a, b = map(int, input().split())
    l.append([a, b])
l.sort(key = lambda x: (x[0], x[1]))
for i in l:
    print(i[0], i[1])