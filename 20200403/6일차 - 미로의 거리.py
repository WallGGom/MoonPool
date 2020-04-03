import sys
sys.stdin = open('6일차 - 미로의 거리.txt','r')

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def chaja(y,x,l):
    global MX
    temp.append([y,x,l])
    visited.append((y,x))

    while temp :
        nxt = temp.pop(0)

        for i in range(4):
            n_y = nxt[0] + dy[i]
            n_x = nxt[1] + dx[i]
            if 0 <= n_y < N and 0 <= n_x < N:
                if Maze[n_y][n_x] == '0' and (n_y,n_x) not in visited:
                    temp.append([n_y,n_x,nxt[2]+1])
                    visited.append((n_y,n_x))
                elif Maze[n_y][n_x] == '3':
                    MX = nxt[2]
                    return

T = int(input())
for tc in range(T):
    N = int(input())
    Maze = [list(input()) for _ in range(N)]
    # print(Maze)
    temp = []
    MX = 0
    visited = []
    for y in range(N):
        for x in range(N):
            if Maze[y][x] == '2':
                chaja(y,x,0)
                break
    print(f'#{tc+1} {MX}')