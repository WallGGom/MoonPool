import sys
sys.stdin = open('5일차 - Magnetic.txt','r')

T = 10
for tc in range(T):
    N = int(input())
    Table = [input().split() for _ in range(N)]
    res = 0
    for sero in zip(*Table):
        res += ''.join(sero).replace('0','').count('12')
    print(f'#{tc+1} {res}')