def val(x, y):
    N = 150
    step = 2
    for _ in range(N):
        if _ == 0:
            ans = 1
            count = 1
        else:
            ans = ans + step
            step += 1
            count += 1
            if count == x:
                stair = x
                for st in range(y-1):
                    ans += stair + st
                break
    return ans

print(val(3,3))