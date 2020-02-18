import sys
sys.stdin = open('홍준이의 숫자 놀이.txt', 'r')

T = int(input())

def hooouuu(a,b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 > 0 :
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r

        s = s1 - q * s2
        s1, s2 = s2, s

        t = t1 - q * t2
        t1, t2 = t2, t
    return s1, t1
ans = []
for tc in range(T):
    A, B = map(int, input().split())
    x, y = hooouuu(A, B)

    print('#{} {} {}'.format(tc+1, x, y))
