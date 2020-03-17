import sys
sys.stdin = open('상호의 배틀필드.txt','r')

Tank = ['^','v','<','>']
joystick = ['U','D','L','R','S']
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def ipryuk(now, sunseo):
    global ans
    if sunseo == N:
        ans = MAP
        return
    
    num = joystick.index(jojong[sunseo])
    if num <= 3:
        MAP[now[0]][now[1]] = Tank[num]
        n_y = now[0] + dy[num]
        n_x = now[1] + dx[num]
        if 0 <= n_y < H and 0 <= n_x < W:
            if MAP[n_y][n_x] == '.':
                MAP[now[0]][now[1]] = '.'
                MAP[n_y][n_x] = Tank[num]
                ipryuk([n_y,n_x],sunseo+1)
            else:
                ipryuk(now,sunseo+1)
        else:
            ipryuk(now,sunseo+1)
        
    else:
        ppangya(now[0],now[1])
        ipryuk(now,sunseo+1)

def ppangya(y,x):
    t_m = True
    n = 1
    num = Tank.index(MAP[y][x])
    while t_m:
        n_y = y + dy[num]*n
        n_x = x + dx[num]*n
        if 0 <= n_y < H and 0 <= n_x < W:
            if MAP[n_y][n_x] == '*':
                MAP[n_y][n_x] = '.'
                t_m = False
            elif MAP[n_y][n_x] == '#':
                t_m = False
            else:
                n += 1
        else:
            t_m = False

T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]
    # print(MAP)
    N = int(input())
    jojong = input()
    # print(jojong)
    ans = []
    t = False
    for y in range(H):
        for x in range(W):
            if MAP[y][x] == '^' or MAP[y][x] == 'v' or MAP[y][x] == '<' or MAP[y][x] == '>':
                ipryuk([y,x],0)
                t = True
                break
        if t:
            break
    res = ''
    for i in ans:
        res += ''.join(i) + '\n'
    print(f'#{tc+1} {res[:len(res)-1]}')