import sys
sys.stdin = open('벽돌 깨기.txt', 'r')

import copy

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def tuhwa(j):
    for y in range(H):
        if temp1[y][j]:
            if temp1[y][j] == 1:
                temp1[y][j] = 0
            else:
                power = temp1[y][j]
                temp1[y][j] = 0
                for k in range(1,power):
                    for l in range(3):
                        n_y = y+(dy[l]*k)
                        n_x = j+(dx[l]*k)
                        if 0 <= n_y < H and 0 <= n_x < W:
                            if temp1[n_y][n_x] == 1:
                                temp1[n_y][n_x] = 0
                            elif temp1[n_y][n_x] > 1:
                                bank.add((n_y,n_x))
        else:
            continue
        return
                
def Kwagwang(loc):
    power = temp1[loc[0]][loc[1]]
    temp1[loc[0]][loc[1]] = 0
    for k in range(1,power):
        for l in range(4):
            n_y = loc[0] + (dy[l] * k)
            n_x = loc[1] + (dx[l] * k)
            if 0 <= n_y < H and 0 <= n_x < W:
                if temp1[n_y][n_x] == 1:
                    temp1[n_y][n_x] = 0
                elif temp1[n_y][n_x] > 1:
                    bank.add((n_y,n_x))


def DDenggyu(lst):
    global t
    cnt2 = 0
    for x in range(W):
        for y in range(H):
            if lst[y][x] == 0:
                for step in range(y):
                    lst[y-step][x], lst[y-step-1][x] = lst[y-step-1][x], lst[y-step][x]
                cnt2 += 1
    if cnt2 == W*H:
        t = False
        

def counter(lst):
    cnt = 0
    for y in range(H):
        for x in range(W):
            if lst[y][x]:
                cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    renga = [[list(map(int, input().split())) for _ in range(H)] for _ in range(1)]
    # print(renga)
    renga2 = [[] for _ in range(W)]
    renga3 = [[] for _ in range(W*W)]
    renga4 = [[] for _ in range(W*W*W)]
    renga5 = [[] for _ in range(W*W*W*W)]
    mn = W*H
    n = 0
    t = True
    while n<N and t:
        if n == 0:
            A_C = renga
        elif n == 1:
            A_C = renga2
        elif n == 2:
            A_C = renga3
        elif n == 3:
            A_C = renga4
        for num, temp0 in enumerate(A_C):
            for i in range(W):
                temp1 = copy.deepcopy(temp0)
                bank = set()
                tuhwa(i)
                while bank:
                    Kwagwang(bank.pop())
                DDenggyu(temp1)
                if n == 0:
                    renga2[i] = copy.deepcopy(temp1)
                elif n == 1:
                    renga3[num*W + i] = copy.deepcopy(temp1)
                elif n == 2:
                    renga4[num*W + i] = copy.deepcopy(temp1)
                elif n == 3:
                    renga5[num*W + i] = copy.deepcopy(temp1)
        n += 1
    if n == 4 and t:
        for i in renga5:
            if counter(i) < mn:
                mn = counter(i)
    elif n == 3 and t:
        for i in renga4:
            if counter(i) < mn:
                mn = counter(i)
    elif n == 2 and t:
        for i in renga3:
            if counter(i) < mn:
                mn = counter(i)
    elif n == 1 and t:
        for i in renga2:
            if counter(i) < mn:
                mn = counter(i)         
    elif t == False:
        mn = 0 
    print(f'#{tc+1} {mn}')

