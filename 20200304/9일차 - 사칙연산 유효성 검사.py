import sys
sys.stdin = open('9일차 - 사칙연산 유효성 검사.txt', 'r')

T = 10
for tc in range(T):
    N = int(input())
    namu = []
    res = 1
    for _ in range(N):
        namu.append(input().split())

    for i in namu:
        if len(i) == 4:
            if i[1].isdecimal():
                res = 0
                break
        else:
            if not i[1].isdecimal():
                res = 0
                break
    print(f'#{tc+1} {res}')