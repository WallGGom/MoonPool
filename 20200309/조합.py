import sys
sys.stdin = open("조합.txt")

T = int(input())
m = 1234567891

def jegop(x, y):
    xy = 1
    while y > 0:
        if (y % 2):
            xy *= x
            y -= 1
            xy %= m
        x *= x
        x %= m
        y /= 2
    return xy

def fac(num):
    if num > 1:
        return num * fac(num-1) % m
    else:
        return 1 

for tc in range(T):
    N, R = map(int, input().split())

    ans_n = fac(N)
    ans_r = fac(R)
    ans_nr = fac(N-R)

    res2 = jegop(ans_r*ans_nr, m-2) % m
    ans_n *= res2
    ans_n %= m

    print(f'#{tc+1} {ans_n}')
