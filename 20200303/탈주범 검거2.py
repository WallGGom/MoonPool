import sys
sys.stdin = open('탈주범 검거.txt','r')

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
banghyang = {0: 1, 1: 0, 2: 3, 3: 2}

def BBiyong(y, x, d):
    global cnt

    if d == L:
        return
 
    for i in able[hasugu[y][x]]:
        n_y = y + dy[i]
        n_x = x + dx[i]
        if 0 <= n_y < N and 0 <= n_x < M and hasugu[n_y][n_x] and Itachi[n_y][n_x] == 0:
            if banghyang[i] in able[hasugu[n_y][n_x]]:
                bank.append([n_y, n_x, d + 1])
                Itachi[n_y][n_x] = 1
                cnt += 1
    if bank:
        BBiyong(*bank.pop(0))
 
T = int(input())
 
for tc in range(T):
    N, M, R, C, L, = map(int, input().split())
    hasugu = [list(map(int, input().split())) for _ in range(N)]
    Itachi = [[0 for i in range(M)] for j in range(N)]
    bank = []
    able = {1: (0, 1, 2, 3), 2: (2, 3), 3: (0, 1), 4: (0, 3), 5: (0, 2), 6: (1, 2), 7: (1, 3)}
    Itachi[R][C] = 1
    cnt = 1
    BBiyong(R, C, 1)
    # print(bank)

    print(f'#{tc+1} {cnt}')