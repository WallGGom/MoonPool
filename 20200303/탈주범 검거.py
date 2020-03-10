import sys
sys.stdin = open('탈주범 검거.txt','r')

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def chajachaja(y,x,cnt):
    Itachi[y][x] = 1

    if cnt == L-1:
        return

    if hasugu[y][x] == 1:
        for k in range(4):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_y < N and 0 <= n_x < M:
                if hasugu[n_y][n_x] in (1,3,6,7) and k == 0:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,3,4,5) and k == 1:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,2,4,7) and k == 2:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,2,5,6) and k == 3:
                    chajachaja(n_y,n_x,cnt+1)
    elif hasugu[y][x] == 2:
        for k in (2,3):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_y < N and 0 <= n_x < M:
                if hasugu[n_y][n_x] in (1,2,4,7) and k == 2:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,2,5,6) and k == 3:
                    chajachaja(n_y,n_x,cnt+1)
    elif hasugu[y][x] == 3:
        for k in (0,1):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_y < N and 0 <= n_x < M:
                if hasugu[n_y][n_x] in (1,3,6,7) and k == 0:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,3,4,5) and k == 1:
                    chajachaja(n_y,n_x,cnt+1)
    elif hasugu[y][x] == 4:
        for k in (0,3):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_y < N and 0 <= n_x < M:
                if hasugu[n_y][n_x] in (1,3,6,7) and k == 0:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,2,5,6) and k == 3:
                    chajachaja(n_y,n_x,cnt+1)
    elif hasugu[y][x] == 5:
        for k in (0,2):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_y < N and 0 <= n_x < M:
                if hasugu[n_y][n_x] in (1,3,6,7) and k == 0:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,2,4,7) and k == 2:
                    chajachaja(n_y,n_x,cnt+1)
    elif hasugu[y][x] == 6:
        for k in (1,2):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_y < N and 0 <= n_x < M:
                if hasugu[n_y][n_x] in (1,3,4,5) and k == 1:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,2,4,7) and k == 2:
                    chajachaja(n_y,n_x,cnt+1)
    elif hasugu[y][x] == 7:
        for k in (1,3):
            n_y = y + dy[k]
            n_x = x + dx[k]
            if 0 <= n_y < N and 0 <= n_x < M:
                if hasugu[n_y][n_x] in (1,3,4,5) and k == 1:
                    chajachaja(n_y,n_x,cnt+1)
                elif hasugu[n_y][n_x] in (1,2,5,6) and k == 3:
                    chajachaja(n_y,n_x,cnt+1)
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    hasugu = [list(map(int, input().split())) for _ in range(N)]
    Itachi = [[0 for i in range(M)] for j in range(N)]
    # print(hasugu)
    # print(Itachi)
    chajachaja(R,C,0)
    # print(Itachi)
    res = 0
    for _ in Itachi:
        res += sum(_)
    # print(res)
    print(f'#{tc+1} {res}')