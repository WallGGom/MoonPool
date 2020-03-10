import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt', 'r')

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def DDakpul(Y,X,res):

    if len(res) == 7:
        bank.add(res)
        return

    for i in range(4):
        n_y = Y + dy[i]
        n_x = X + dx[i]

        if 0 <= n_y <= 3 and 0 <= n_x <= 3:
            DDakpul(n_y,n_x,res+Table[n_y][n_x])

T = int(input())
for tc in range(T):
    Table = [list(input().split()) for _ in range(4)]
    # print(Table)
    bank = set()
    for y in range(4):
        for x in range(4):
            DDakpul(y,x,Table[y][x])
    print(f'#{tc+1} {len(bank)}')