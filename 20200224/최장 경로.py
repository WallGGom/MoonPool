import sys
sys.stdin = open('최장 경로.txt', 'r')

T = int(input())

def gil(n):
    global MX, cnt

    if cnt > MX:
        MX = cnt

    for i in range(1,N+1):
        if Table[n][i] == 1 and check[i-1] == 0:
            # Table [n][i] = 0
            cnt += 1
            check[i-1] = 1
            gil(i)
            # Table [n][i] = 1
            cnt -= 1
            check[i-1] = 0


for tc in range(T):
    N, M = map(int, input().split())
    Table = [[0 for i in range(N+1)] for j in range(N+1)]
    check = [0]*N
    MX = 0
    cnt = 0
    for _ in range(M):
        x, y = map(int, input().split())
        Table[y][x] = 1
        Table[x][y] = 1

    
    for y in range(1,N+1):
        check[y-1] = 1
        gil(y)
        check[y-1] = 0
    print(f'#{tc+1} {MX+1}')



