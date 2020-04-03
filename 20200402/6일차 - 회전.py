import sys
sys.stdin = open('6일차 - 회전.txt','r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    suyeol = list(input().split())

    for i in range(M):
        suyeol.append(suyeol.pop(0))
    print(f'#{tc+1} {suyeol[0]}')