import sys
sys.stdin = open('디저트 카페.txt','r')

dy=[1, -1, -1, 1]
dx=[1, 1, -1, -1]
 
def sagak(y, x, ind, tour):
    global MX
    if ind == 4:
        return
    
    n_y = y + dy[ind]
    n_x = x + dx[ind]
    if 0 <= n_y < N and 0 <= n_x < N:
        if n_y == i and n_x == j:
            if len(tour) > MX:
                MX = len(tour)
                return
        if Cafe[n_y][n_x] not in tour:
            tour.append(Cafe[n_y][n_x])
            sagak(n_y, n_x, ind, tour)
            sagak(n_y, n_x, ind+1, tour)
            tour.pop()
 
T = int(input())
for tc in range(T):
    N = int(input())
    Cafe = [list(map(int, input().split())) for _ in range(N)]
    MX = -1
 
    for i in range(1,N-1):
        for j in range(N-2):
            sagak(i, j, 0, [Cafe[i][j]])

    print(f'#{tc+1} {MX}')