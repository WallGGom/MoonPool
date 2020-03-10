import sys
sys.stdin = open('4일차 - 보급로.txt', 'r')

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

T = int(input())
for tc in range(T):
    N = int(input())
    land = [list(map(int, input())) for _ in range(N)]
    t = [[9*(N+2)]*N for _ in range(N)]
    # print(land)
    # print(t)
    bank = [(0,0)]
    t[0][0] = 0
    while bank:
        y, x = bank.pop(0)
        for i in range(4):
            n_y = y + dy[i]
            n_x = x + dx[i]
            if 0 <= n_y < N and 0 <= n_x < N:
                if t[n_y][n_x] > land[n_y][n_x] + t[y][x]:
                    t[n_y][n_x] = land[n_y][n_x] + t[y][x]
                    bank.append((n_y,n_x))
    print(f'#{tc+1} {t[N-1][N-1]}')