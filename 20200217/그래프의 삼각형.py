import sys
sys.stdin = open('그래프의 삼각형.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Table = [[0 for i in range(N+1)] for j in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        Table[y][x] = 1
        Table[x][y] = 1
    # print(Table)

    ans = 0
    for i in range(1,N+1):
        temp = []
        for j in range(1,N+1):
            if Table[i][j] == 1:
                temp.append(j)
        # print(temp)
        for k in temp:
            for l in temp[temp.index(k):]:
                if Table[k][l] == 1:
                    ans += 1
    print('#{} {}'.format(tc+1, ans//3))

