import sys
sys.stdin = open('7일차 - 미로1.txt', 'r')

Drx = [-1, 0, 1, 0]
Dry = [0, -1, 0, 1]


def DFS(y, x):
    global res
    for n in range(4):
        n_y = y + Dry[n]
        n_x = x + Drx[n]
        if maze[n_y][n_x] == 3:
            res = 1
            return
        elif maze[n_y][n_x] == 0 and not [n_y, n_x] in visited:
            visited.append([n_y, n_x])
            DFS(n_y, n_x)
        elif maze[n_y][n_x] == 0 and [n_y, n_x] in visited:
            maze[y][x] = 1
            DFS(n_y, n_x)

T = 10
for tc in range(T):
    t = int(input())
    maze = [[0]*16 for _ in range(16)]
    for i in range(16):
        x = 0
        for j in input():
            maze[i][x] = int(j)
            x += 1
    # print(maze)

    start = []
    for y in range(16):
        if start:
            break
        for x in range(16):
            if maze[y][x] == 2:
                start = [y, x]
                break
    # print(start)
    visited = []
    res = 0
    DFS(start[0],start[1])
    print('#{} {}'.format(t, res))
