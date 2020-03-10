import sys
sys.stdin = open('정사각형 방.txt','r')
sys.setrecursionlimit(3000)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def chajachaja(y,x):
    global cnt

    for k in range(4):
        n_y = y + dy[k]
        n_x = x + dx[k]
        if 0 <= n_y < N and 0 <= n_x < N:
            if Table[n_y][n_x] == Table[y][x] + 1:
                cnt += 1
                chajachaja(n_y,n_x)
                break
        

T = int(input())
for tc in range(T):
    N = int(input())
    Table = [list(map(int, input().split())) for _ in range(N)]
    # print(Table)

    MX = 0
    res = N**2
    ans = {}
    for i in range(N):
        for j in range(N):
            t = True
            for k in range(4):
                n_y = i + dy[k]
                n_x = j + dx[k]
                if 0 <= n_y < N and 0 <= n_x < N:
                    if Table[i][j] == Table[n_y][n_x] + 1:
                        t = False
                        break
            if t:
                cnt = 1
                chajachaja(i,j)
                if cnt > MX:
                    ans[Table[i][j]] = cnt
    for key, value in ans.items():
        if value == max(ans.values()) and key < res:
            res = key

    print(f'#{tc+1} {res} {max(ans.values())}')