import sys
sys.stdin = open('5일차 - 미로.txt', 'r')

Drx = [-1, 0, 1, 0]
Dry = [0, -1, 0, 1]

def DFS(y, x):
    global res
    if res == 1:
        return
    for n in range(4):
        n_y = y + Dry[n]
        n_x = x + Drx[n]
        if 0 <= n_y < N and 0 <= n_x < N:
            if maze[n_y][n_x] == 3:
                res = 1
                return
            elif maze[n_y][n_x] == 0 and not [n_y, n_x] in visited:
                visited.append([n_y, n_x])
                DFS(n_y, n_x)
            elif maze[n_y][n_x] == 0 and [n_y, n_x] in visited:
                maze[y][x] = 1
                DFS(n_y, n_x)

T = int(input())

for tc in range(T):
    N = int(input())
    maze = [[int(_) for _ in list(input())] for _ in range(N)]
    # print(maze)

    start = []
    for y in range(N-1,-1,-1):
        if start:
            break
        for x in range(N):
            if maze[y][x] == 2:
                start = [y, x]
                break
    # print(start)

    visited = []
    res = 0
    DFS(start[0],start[1])

    print('#{} {}'.format(tc+1, res))