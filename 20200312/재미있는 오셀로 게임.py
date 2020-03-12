import sys
sys.stdin = open('재미있는 오셀로 게임.txt','r')

dy = [0,0,-1,1,1,1,-1,-1]
dx = [-1,1,0,0,1,-1,-1,1]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Table = [[0 for i in range(N)] for j in range(N)]
    Table[N//2][N//2] = Table[N//2-1][N//2-1] = 2
    Table[N//2-1][N//2] = Table[N//2][N//2-1] = 1
    # print(Table)
    
    for __ in range(M):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1
        Table[y][x] = c
        for i in range(8):
            t = True
            temp = []
            n = 1
            while t:
                n_x = x + dx[i]*n
                n_y = y + dy[i]*n
                if 0 <= n_x < N and 0 <= n_y < N:
                    if c == 1:
                        if Table[n_y][n_x] == 2:
                            temp.append([n_x,n_y])
                            n += 1
                        elif Table[n_y][n_x] == 1:
                            while temp:
                                loc = temp.pop()
                                Table[loc[1]][loc[0]] = 1
                            t = False
                        else:
                            t = False
                    elif c == 2:
                        if Table[n_y][n_x] == 1:
                            temp.append([n_x,n_y])
                            n += 1
                        elif Table[n_y][n_x] == 2:
                            while temp:
                                loc = temp.pop()
                                Table[loc[1]][loc[0]] = 2
                            t = False
                        else:
                            t = False

                else:
                    t = False
        
    cnt_B = 0
    cnt_W = 0
    for y in range(N):
        for x in range(N):
            if Table[y][x] == 1:
                cnt_B += 1
            elif Table[y][x] == 2:
                cnt_W += 1
    print(f'#{tc+1} {cnt_B} {cnt_W}')

