import sys
sys.stdin = open('두 개의 숫자열1.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))

    # print(list_A, list_B)

    MX = 0
    for i in range(abs(N-M)+1):
        hap = 0
        for j in range(min(N,M)):
            if N < M:
                hap += list_A[j] * list_B[j+i]
            elif M < N:
                hap += list_B[j] * list_A[j + i]
            elif N == M:
                hap += list_B[j] * list_A[j]
        if MX < hap:
            MX = hap

    print('#{} {}'.format(tc+1,MX))
