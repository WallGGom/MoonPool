import sys
sys.stdin = open('가장 빠른 문자열 타이핑.txt', 'r')

T = int(input())

for tc in range(T):
    A, B = map(str, input().split())

    cnt = 0
    t = True
    res = ''
    while t:
        if B in A:
            A = A[:A.find(B)] + A[A.find(B)+len(B):]
            cnt += 1
        else:
            t = False
    cnt += len(A)
    print(f'#{tc+1} {cnt}')
