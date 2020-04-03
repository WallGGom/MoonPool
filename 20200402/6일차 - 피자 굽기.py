import sys
sys.stdin = open('6일차 - 피자 굽기.txt','r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append([i,pizza[i]])

    j = 0
    while len(Q) > 1:
        Q[0][1] //= 2
        
        nxt = Q.pop(0)
        if nxt[1] == 0:
            if N + j < M:
                Q.append([N+j,pizza[N+j]])
                j += 1
        else:
            Q.append(nxt)

    print(f'#{tc+1} {Q[0][0]+1}')