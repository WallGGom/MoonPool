import sys
sys.stdin = open('동철이의 일 분배.txt', 'r')

def ilhera(i,prb):
    global MX
    if prb <= MX:
        return

    if i == N-1:
        if prb > MX:
            MX = prb
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            ilhera(i+1,prb*(hatsan[i+1][j]/100))
            visited[j] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    hatsan = [list(map(int, input().split())) for _ in range(N)]
    # print(hatsan)
    visited = [0] * N
    MX = 0
    for i in range(N):
        visited[i] = 1
        ilhera(0,hatsan[0][i]/100)
        visited[i] = 0
    # print(MX)
    print(f'#{tc+1} {MX*100:.6f}')