def pow(a, n, m):
    s = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            s = [[(s[0][0] * a[0][0] + s[0][1] * a[1][0]) % m, (s[0][0] * a[0][1] + s[0][1] * a[1][1]) % m], [(s[1][0] * a[0][0] + s[1][1] * a[1][0]) % m, (s[1][0] * a[0][1] + s[1][1] * a[1][1]) % m]]
        a = [[(a[0][0] * a[0][0] + a[0][1] * a[1][0]) % m, (a[0][0] * a[0][1] + a[0][1] * a[1][1]) % m], [(a[1][0] * a[0][0] + a[1][1] * a[1][0]) % m, (a[1][0] * a[0][1] + a[1][1] * a[1][1]) % m]]
        n //= 2
    return s
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = [[1, 1], [1, 0]]
    s = pow(f, n - 1, 1000000007)
    return s[0][0]
n = int(input())
print(fibo(n))