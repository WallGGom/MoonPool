import sys
sys.stdin = open('7일차 - 행렬찾기.txt', 'r')

def Serosirung(x):
    global g

    if Table[Y][x] == 0:
        g = x
        return

    elif x == N-1:
        g = x
        return 

    elif Table[Y][x] and x < N:
        Serosirung(x+1)
    
def Garosirung(y):
    global s

    if Table[y][X] == 0:
        s = y
        return

    elif y == N-1:
        s = y
        return

    elif Table[y][X] and y < N:
        Garosirung(y+1)

T = int(input())

for tc in range(T):
    N = int(input())
    Table = [list(map(int, input().split())) for _ in range(N)]
    res = []
    for Y in range(N):
        for X in range(N):
            s = 0
            g = 0
            if Table[Y][X]:
                start = [Y, X]
                if Y + 1 < N and X + 1 < N:
                    if Table[Y][X+1]:
                        Serosirung(X+1)
                    else:
                        g = X + 1
                    if Table[Y+1][X]:
                        Garosirung(Y+1)
                    else:
                        s = Y + 1
                elif X == N-1:
                    if Table[Y+1][X]:
                        Garosirung(Y+1)
                elif Y == N-1:
                    if Table[Y][X+1]:
                        Serosirung(X+1)

            if s != 0 and g != 0:
                for i in range(Y,s):
                    for j in range(X,g):
                        Table[i][j] = 0
                res.append([str(s-Y),str(g-X)])

    ans = sorted(res, key=lambda x:(int(x[0])*int(x[1]),int(x[0])))
    f =''
    for _ in ans:
        f += ' '.join(_) + ' '
    print(f'#{tc+1} {len(res)} {f}')


