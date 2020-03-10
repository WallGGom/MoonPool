def cal():
    state = [(0,0)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    map_time[0][0] = 0
    while state:
        r, c = state.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0<= nr < N and 0<= nc < N):
                continue
            if map_time[nr][nc] > map_time[r][c] + matrix[nr][nc]:
                map_time[nr][nc] = map_time[r][c] + matrix[nr][nc]
                state.append((nr, nc))
 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    map_time = [[float('inf')]*N for _ in range(N)]
    cal()
    print('#{} {}'.format(tc, map_time[N-1][N-1]))