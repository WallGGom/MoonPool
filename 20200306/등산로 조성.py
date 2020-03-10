import sys
sys.stdin = open('등산로 조성.txt', 'r')

import copy

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def hiking(y,x,cnt,sapjil,Table):
    global MX_L
    if MX_L < cnt:
        MX_L = cnt
    for j in range(4):
        n_y = y + dy[j]
        n_x = x + dx[j]
        if 0 <= n_y < N and 0 <= n_x < N:
            if visit[n_y][n_x] == 0:
                if Table[y][x] > Table[n_y][n_x]:
                    visit[n_y][n_x] = 1
                    hiking(n_y,n_x,cnt+1,sapjil,Table)
                    visit[n_y][n_x] = 0
                elif Table[y][x] <= Table[n_y][n_x]:
                    if sapjil == False:
                        for depth in range(1,K+1):
                            if Table[y][x] > Table[n_y][n_x] - depth:
                                n_Table = copy.deepcopy(Table)
                                n_Table[n_y][n_x] = Table[n_y][n_x] - depth
                                visit[n_y][n_x] = 1
                                hiking(n_y,n_x,cnt+1,True,n_Table)
                                visit[n_y][n_x] = 0
                                break
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    Mt = [list(map(int, input().split())) for _ in range(N)]

    start = set()
    MX_H = 0
    for y in range(N):
        for x in range(N):
            if MX_H < Mt[y][x]:
                MX_H = Mt[y][x]
                start.clear()
                start.add((y,x))
            elif MX_H == Mt[y][x]:
                start.add((y,x))

    MX_L = 0
    visit = [[0]*N for _ in range(N)]
    for i in start:
        visit[i[0]][i[1]] = 1
        hiking(i[0],i[1],1,False,Mt)
        visit[i[0]][i[1]] = 0
    print(f'#{tc+1} {MX_L}')

