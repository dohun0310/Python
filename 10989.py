import sys
r = int(sys.stdin.readline())
l = [0] * 10001
for i in range(r):
    l[int(sys.stdin.readline())] += 1
for i in range(10001):
    if l[i] != 0:
        for j in range(l[i]):
            print(i)