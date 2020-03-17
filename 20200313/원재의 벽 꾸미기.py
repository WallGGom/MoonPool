import sys
sys.stdin = open('원재의 벽 꾸미기.txt','r')

T = int(input())
for tc in range(T):
    N, A, B = list(map(int, input().split()))
    R = 0
    sagak = []
    t = True
    while t:
        R += 1
        C = N // R
        if N >= R*R:
            sagak.append([R, C])
        else:
            sagak.append([R-1,R-1])
            t = False
    # print(sagak)

    ans = 10000000000
    for i in sagak:
        k = A * (abs(i[0] - i[1])) + B * (N - (i[0] * i[1]))
        if ans > k:
            ans = k
    print(f'#{tc+1} {ans}')