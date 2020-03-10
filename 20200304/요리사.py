import sys
sys.stdin = open('요리사.txt', 'r')

def nikkeonekkeo(n,pick):
    if n == M/2 and len(pick) == 0:
        return
    if len(pick) == M//2:
        bank.append(pick)
        return
    if n == M-1:
        return
    else:
        nikkeonekkeo(n+1,pick + [])
        nikkeonekkeo(n+1,pick + [n+1])

def mimi(n, lst):
    if n == (M//2)-2 and len(lst) == 0:
        return
    if len(lst) == 2:
        temp1.append(lst)
        return
    if n == (M//2)-1:
        return
    else:
        mimi(n+1,lst + [])
        mimi(n+1,lst + [i[n+1]])

sol = {}
for M in range(4,17,2):
    bank = []
    nikkeonekkeo(0,[])
    nikkeonekkeo(0,[0])
    bank.sort()

    temp2 = []
    for i in bank:
        temp1 = []
        mimi(0,[])
        mimi(0,[i[0]])
        temp2.append(temp1)
    sol[M] = temp2

T = int(input())
for tc in range(T):
    N = int(input())
    Si = [list(map(int, input().split())) for _ in range(N)]
    # print(Si)

    mn = 20000*8
    for ind, j in enumerate(sol[N]):
        A = 0
        B = 0
        for k in sol[N][ind]:
            a_y,a_x = k
            # print(a_y,a_x)
            A += Si[a_y][a_x] + Si[a_x][a_y]
        for l in sol[N][len(sol[N]) - ind - 1]:
            b_y,b_x = l
            # print(b_y,b_x)
            B += Si[b_y][b_x] + Si[b_x][b_y]
        total = abs(A - B)
        if mn > total:
            mn = total
    print(f'#{tc+1} {mn}')