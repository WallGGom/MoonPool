n = int(input())

for y in range(0, n):
    for x in range(0, n):
        R = min(x, y, (n - 1) - x, (n - 1) - y)
        if x >= y:
            q = x + y - 2 * R
        else:
            q = ((n - 1) - (2 * R)) * 4 - (x + y - 2 * R)
        q += 4 * (n - R) * R
        print("{}".format(q))


