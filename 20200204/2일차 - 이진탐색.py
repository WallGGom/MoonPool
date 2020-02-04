import sys
sys.stdin = open('2일차 - 이진탐색.txt', 'r')

T = int(input())

for tc in range(T):
    P, A, B = map(int, input().split())

    # print(P, A, B)
    Ap, Aa, Ab = P, A, B
    Bp, Ba, Bb = P, A, B

    # A
    cntA = 0
    ansA = 1
    while ansA != A:
        if Aa >= (ansA + Ap)/2:
            ansA = (ansA + Ap)//2
            cntA += 1
        elif Aa < (ansA + Ap)/2:
            Ap = (ansA + Ap)//2
            cntA += 1

    cntB = 0
    ansB = 1
    while ansB != B:
        if Bb >= (ansB + Bp)/2:
            ansB = (ansB + Bp)//2
            cntB += 1
        elif Bb < (ansB + Bp)/2:
            Bp = (ansB + Bp)//2
            cntB += 1

    if cntA > cntB:
        result = 'B'

    elif cntA < cntB:
        result = 'A'

    elif cntA == cntB:
        result = '0'

    print('#{} {}'.format(tc+1, result))

