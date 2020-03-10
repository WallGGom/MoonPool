import sys
sys.stdin = open('삼성시의 버스 노선.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    bus = [0]*5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A,B+1):
            bus[i] += 1
    P = int(input())
    res = ''
    for _ in range(P):
        stop = int(input())
        res += str(bus[stop]) + ' '
    print(f'#{tc+1} {res}')
