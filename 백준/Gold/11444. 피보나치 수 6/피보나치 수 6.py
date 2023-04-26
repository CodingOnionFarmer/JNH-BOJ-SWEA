fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
fib_big = {}


def shrink(n):
    if n < 18:
        return fib[n]
    if n in fib_big:
        return fib_big[n]
    if n % 2:
        ans = (shrink(n // 2 + 1) ** 2 + shrink(n // 2) ** 2) % 1000000007
    else:
        ans = (shrink(n // 2) ** 2 + 2 * shrink(n // 2) * shrink(n // 2 - 1)) % 1000000007
    fib_big[n] = ans
    return ans


print(shrink(int(input())))
